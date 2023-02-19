# Assume the worker nodes have performed the data analysis tasks and returned their results to the master node
# The master node has stored the results in a dictionary with product names as keys and a tuple of (total units sold, average units sold per day) as values
worker_results = {
    "Product A": (100, 5),
    "Product B": (200, 10),
    "Product C": (150, 7.5),
}

# Sorting the results by the total units sold to determine the rank of each product
sorted_results = sorted(worker_results.items(), key=lambda x: x[1][0], reverse=True)

# Adding the rank to each product in the results
for i, result in enumerate(sorted_results):
    product, (total, avg) = result
    sorted_results[i] = (product, (total, avg), i+1)

# Generating the HTML report
html = """
<html>
<head>
  <style>
    table {
      border-collapse: collapse;
    }
    th, td {
      border: 1px solid black;
      padding: 5px;
    }
  </style>
</head>
<body>
  <h2>Sales Report</h2>
  <table>
    <tr>
      <th>Rank</th>
      <th>Product</th>
      <th>Total Units Sold</th>
      <th>Average Units Sold per Day</th>
    </tr>
"""

for result in sorted_results:
    product, (total, avg), rank = result
    html += f"<tr><td>{rank}</td><td>{product}</td><td>{total}</td><td>{avg}</td></tr>"

html += """
  </table>
</body>
</html>
"""

# Writing the HTML report to a file
with open("sales_report.html", "w") as file:
    file.write(html)

