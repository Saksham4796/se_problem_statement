FROM mysql:latest

ENV MYSQL_DATABASE SALES_DATABASE

# Copy the SQL dump file to the container
COPY ./scripts/ /docker-entrypoint-initdb.d/
