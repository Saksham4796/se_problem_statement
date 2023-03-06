import pandas as pd

# Read CSV file into pandas DataFrame
df = pd.read_csv('total_sales_merged.csv')

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
    {html_table}
   </body>
</html>
''')
