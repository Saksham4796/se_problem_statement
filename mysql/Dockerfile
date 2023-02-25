FROM mysql:latest

ENV MYSQL_DATABASE SALES_DATABASE

COPY sales_data_sample.csv /var/lib/mysql-files/sales_data_sample.csv

# Copy the SQL dump file to the container
COPY ./scripts/ /docker-entrypoint-initdb.d/
