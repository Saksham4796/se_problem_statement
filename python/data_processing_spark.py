from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, month, year, to_date
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType

import os
import mysql.connector
import pandas as pd

os.system("rm -rf total_sales.csv")

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

total_sales.write.csv("total_sales.csv", header=True)
os.system("cat total_sales.csv/part-* > total_sales_merged.csv")
