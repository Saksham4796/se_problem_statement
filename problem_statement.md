## Problem Statement: Distributed Data Analytics for Sales Performance using MySQL Database and Redis

Your company has recently started tracking sales data for its products and has stored the information in a MySQL database. The database contains information about sales for each product, including the date, product name, and the number of units sold. Your company would like to have a quick and easy way to analyze the sales data to gain insights into the performance of each product.

#### Objective: 
Develop a distributed software application that will extract sales data from the MySQL database, perform data analysis tasks on the data, and display the results in a HTML file.

The application should perform the following tasks:

#### Extract data: 
The master node should extract sales data for each product from the MySQL database using SQL queries and store it in a data structure in Redis. The master node should be able to connect to the database using a secure connection and should have the ability to retrieve data based on specific dates, product names, etc.

#### Data analysis: 
The worker nodes should perform the following data analysis tasks on the extracted sales data:

1. Calculate the total number of units sold for each product

2. Determine the average number of units sold per day for each product

3. Identify the top-selling product in terms of total units sold

#### HTML report: 
The master node should generate an HTML report that summarizes the results of the data analysis. The report should include the following information for each product:
Total units sold
Average units sold per day
Rank based on total units sold (e.g. 1st, 2nd, 3rd, etc.)

The HTML report should be easy to understand and visually appealing, with clear and concise graphics, charts, and tables. The report should also be interactive, allowing users to quickly access the data they need by clicking on different sections of the report.

#### Final Deliverable:
Your task is to develop the distributed software application that meets these requirements using Redis for data distribution and coordination between the master node and worker nodes. The solution should be efficient, scalable, and easy to maintain. You should use a programming language such as Python, Java, or C# to develop the application and should have a good understanding of SQL, databases, and Redis.
