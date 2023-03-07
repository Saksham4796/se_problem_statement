from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, month, year, to_date, desc, rank
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType
from pyspark.sql.window import Window

import os
import mysql.connector
import pandas as pd

os.system("rm -rf csv_files")

# Create a Spark session
spark = SparkSession.builder.appName("MySQL_data_processing_with_PySpark").getOrCreate()

# Connect to the MySQL database
conn = mysql.connector.connect(user='root', password='sak479619', host='custom_mysql', database='SALES_DATABASE')
cursor = conn.cursor()

# Extract sales data from MySQL using SQL queries
query = "SELECT Quantity_Ordered, Price_Each, Product_Line, Status, Order_Date FROM sales_data"
cursor.execute(query)
sales_d = cursor.fetchall()

sales_data = [(row[0], float(row[1]), row[2], row[3], row[4]) for row in sales_d]

# Define the schema of the DataFrame
schema = StructType([
    StructField("Quantity_Ordered", IntegerType(), True),
    StructField("Price_Each", FloatType(), True),
    StructField("Product_Line", StringType(), True),
    StructField("Status", StringType(), True),
    StructField("Order_Date", StringType(), True)
])

sales_df = spark.createDataFrame(sales_data,schema=schema)

sales_df.show()


# Filter only shipped orders
shipped_sales_df = sales_df.filter(col("Status") == "Shipped")
shipped_sales_df.show()

# convert the date string to date object and extract year and month
df = shipped_sales_df
# use to_date to convert the date string to a datetime object
df = df.withColumn('date', to_date('Order_Date', 'M/d/y H:mm'))

# use year and month functions to extract the year and month
df = df.withColumn('Year', year('date')).withColumn('Month', month('date'))
df.show()

# group the data by Product_Line, Year, and Month, and compute the total sales
total_sales = df.groupBy("Year", "Month", "Product_Line").agg(sum(col("Quantity_Ordered") * col("Price_Each")).alias("Total_Sales"))
total_sales = total_sales.orderBy("Year", "Month", "Product_Line")

# display the result
total_sales.show()

# Compute the total units sold for each product every year
units_sold_df = df.groupBy("Year", "Month", "Product_Line").agg(sum("Quantity_Ordered").alias("Total_Units_Sold"))
units_sold_df.show()

# Sort the result DataFrame by Year and Total_Units_Sold in descending order
sorted_df = units_sold_df.orderBy(["Year", "Month", "Total_Units_Sold"], ascending=[True, True, False])
sorted_df.show()

total_sales.write.csv("csv_files/total_sales", header=True)
os.system("cat csv_files/total_sales/part-* > csv_files/total_sales_merged.csv")

sorted_df.write.csv("csv_files/item_sale", header=True)
os.system("cat csv_files/item_sale/part-* > csv_files/item_sale_merged.csv")
