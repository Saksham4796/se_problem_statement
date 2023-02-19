LOAD DATA INFILE '/var/lib/mysql-files/sales_data_sample.csv'
INTO table sales_data
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
