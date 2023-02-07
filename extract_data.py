import mysql.connector
import redis

# Connect to the MySQL database
conn = mysql.connector.connect(user='username', password='password', host='hostname', database='database')
cursor = conn.cursor()

# Connect to Redis
redis_conn = redis.Redis(host='localhost', port=6379, db=0)

# Extract sales data from MySQL using SQL queries
query = "SELECT product_name, date, units_sold FROM sales"
cursor.execute(query)
sales_data = cursor.fetchall()

# Store the extracted data in Redis
for data in sales_data:
    product_name, date, units_sold = data
    key = f"{product_name}:{date}"
    redis_conn.set(key, units_sold)

# Allow the master node to retrieve data based on specific dates, product names, etc.
def retrieve_data(product_name, date):
    key = f"{product_name}:{date}"
    units_sold = redis_conn.get(key)
    if units_sold:
        return int(units_sold)
    return None

# Example usage
units_sold = retrieve_data("Product 1", "2022-01-01")
print(units_sold)
