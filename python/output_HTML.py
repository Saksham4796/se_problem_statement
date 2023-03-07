import pandas as pd

# Read first CSV file into pandas DataFrame
df1 = pd.read_csv('csv_files/item_sale_merged.csv')

# Read second CSV file into pandas DataFrame
df2 = pd.read_csv('csv_files/total_sales_merged.csv')

# Concatenate the two DataFrames along the columns axis
df = pd.concat([df1, df2], axis=1)

# Convert DataFrame to HTML table with specified CSS class
html_table = df.to_html(classes='table', index=False)

# Write HTML table to file with specified CSS style
with open('output.html', 'w') as f:
    f.write(f'''
<!DOCTYPE html>
<html>
  <head>
    <title>My CSV Data</title>
    <style>
      table {{
        border-collapse: collapse;
        width: 100%;
        margin-bottom: 20px;
      }}

      th, td {{
        text-align: left;
        padding: 8px;
        border-bottom: 1px solid #ddd;
      }}

      th {{
        background-color: #f2f2f2;
        font-weight: bold;
      }}

      tr:hover {{
        background-color: #f5f5f5;
      }}

      td.number {{
        text-align: right;
      }}

      td.boolean {{
        text-align: center;
      }}

      td.date {{
        text-align: center;
      }}

      @media screen and (max-width: 600px) {{
        table, thead, tbody, th, td, tr {{
          display: block;
        }}

        th {{
          position: absolute;
          top: -9999px;
          left: -9999px;
        }}

        td {{
          border-bottom: none;
          position: relative;
          padding-left: 50%;
        }}

        td:before {{
          position: absolute;
          top: 6px;
          left: 6px;
          width: 45%;
          padding-right: 10px;
          white-space: nowrap;
          content: attr(data-label);
          font-weight: bold;
        }}
      }}
    </style>
    <script src="./website.js"></script>
   </head>
   <body>
    <h2>Items sorted in the descending order of their per Unit sale every month</h2>
    {df1.to_html(classes='table', index=False)}
    <h2>Total Sale for each Item every month</h2>
    {df2.to_html(classes='table', index=False)}
   </body>
</html>
''')

