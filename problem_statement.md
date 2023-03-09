## Problem Statement: Application performing data analytics for Sales Performance using MySQL Database

The company ‘X’ has recently started tracking sales data for its products and has stored the information in a MySQL database. The database contains information such as quantity ordered for each product, price of each product on the date of Order, name of the product, Status(meaning the Product has been shipped or not), Date on which the product was ordered. The company ‘X’ would like to have a quick and easy way to analyze the sales data to gain insights into the performance of each product.

#### Objective: 
Develop a distributed software application using Spark that will extract sales data from the MySQL database, perform data analysis tasks on the data, and display the results in a HTML file. 

The application should perform the following tasks:

#### Create MySQL Database: 
Take a sample\_data.csv file as input and store it in a MySQL database. This MySQL database should be stored a docker container. Write the Dockerfile which creates this database and stores the data present in the sample_data.csv file as a table.

#### Design the Data Processing Application: 
Write a python script which imports the data from MySQL database and performs data processing task such as:
1. Calculates total sale for each time every month.
2. Ranks item based on total units sold every month.

The data processing task is to be performed using PySpark. The input data should be stored in the form of Dataframes and the output should be stored in the csv files. For both the task (1) and (2), two separate csv files should be produced as output.

#### HTML report: 
Also, write a python script which takes these two csv files as input and stores them in a single HTML file. The HTML file needs to be beautified using CSS and javascript.

This complete application(data processing task and storing in HTML file) is to be stored in a separate Docker container. Write a Dockerfile which stores in this application and also installs PySpark and all it’s dependencies. The Dockerfile should also set up all the environment variable so that PySpark and all the essential libraries are fully functional.

#### Integrating all the components:
Finally, write a docker-compose.yml file which establishes a connection between the Docker container which stores the data in MySQL and the Docker container which stores the python application.
