import mysql.connector
import redis
import pandas as pd

# Connect to the MySQL database
conn = mysql.connector.connect(user='root', password='sak479619', host='localhost', database='sales_db')
cursor = conn.cursor()

# Connect to Redis
redis_conn = redis.Redis(host='localhost', port=6379, db=0)

# Extract sales data from MySQL using SQL queries
query = "SELECT Quantity_Ordered, Price_Each, Product_Line, Status, Order_Date FROM sales_data"
cursor.execute(query)
sales_data = cursor.fetchall()

from datetime import datetime

# Initialize an empty dictionary to store total sales
total_sales = {}

# Loop through the sales data
for sale in sales_data:
    quantity, price, commodity, status, date_str = sale
    
    # Check if the commodity was shipped
    if status == 'Shipped':
        # Convert the date string to a datetime object
        date_obj = datetime.strptime(date_str, '%m/%d/%Y %H:%M')
        
        # Extract the month from the datetime object
        month = date_obj.month
        year = date_obj.year
        
        if year not in total_sales.keys():
            total_sales[year]={}
            
        if month not in total_sales[year].keys():
            total_sales[year][month]={}
        
        if commodity not in total_sales[year][month].keys():
            total_sales[year][month][commodity] = 0

        # Add the sale price to the total sales for the commodity and month
        total_sales[year][month][commodity] += quantity * price

# Print the total sales for each commodity for each month of the year

# Create an empty list to hold the rows of the table
table_rows = []

# Loop over the dictionary to extract the data
for y in total_sales.keys():
    for m in total_sales[y].keys():
        for c in total_sales[y][m].keys():
            # Create a tuple with the data
            row = (y, m, c, total_sales[y][m][c])
            # Append the tuple to the list of rows
            table_rows.append(row)

# Convert the list of rows to a pandas DataFrame
df = pd.DataFrame(table_rows, columns=['Year', 'Month', 'Commodity', 'Total Sale'])

# Display the DataFrame
print(df)

# Store the dataframe to a csv file
sorted_df = df.sort_values(['Year', 'Month'])
sorted_df.to_csv('total_sales.csv', index=False)
