import redis

# Connect to the Redis database
r = redis.Redis(host='localhost', port=6379, db=0)

# Retrieve the sales data from Redis
sales_data = r.get('sales_data')

# Convert the sales data from bytes to a dictionary
sales_data = eval(sales_data.decode('utf-8'))

# Create a dictionary to store the results of the data analysis
results = {}

# Loop through each product in the sales data
for product, product_data in sales_data.items():
    total_units_sold = 0
    total_days = len(product_data)
    # Loop through each day's data for the product
    for day, units_sold in product_data.items():
        total_units_sold += units_sold
    # Calculate the average number of units sold per day
    avg_units_sold_per_day = total_units_sold / total_days
    # Store the results in the results dictionary
    results[product] = {'total_units_sold': total_units_sold, 'avg_units_sold_per_day': avg_units_sold_per_day}

# Identify the top-selling product
top_selling_product = max(results, key=lambda x: results[x]['total_units_sold'])

# Store the results in Redis
r.set('results', str(results))
r.set('top_selling_product', top_selling_product)
