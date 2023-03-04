# Software Engineering Problem

This repository holds a problem statement prominent in the software industry. The problem statement has been partly generated using a generative model called chatGPT. The software application satisfying the requirements of the given problem statement has also been developed using chatGPT.

The `mysql` directory is used to build the docker container which contains the Database. The `sales_data_sample.csv` file contains the sample sales data for the problem statement and is uploaded to the MySQL database. The `Dockerfile` is used to build the docker image which contains the Sales data hosted on MySQL database. The `scripts` folder contains .sql files which can build the database on the docker container. 

The `python` folder is used to build the docker container which performs data processing tasks on the dataset. The `data_processing_spark.py` file performs data processing operation using Pyspark(so that data is processing using distributed computing fashion) on the dataset and thus stores total sale for each commodity for each month of the year in the `total_sales.csv` file.

The `docker-compose.yml` file builds both the docker containers and also make a connection between them.

This distributed application is executed on virtual machine intances present on google cloud platform. [VM Instance](https://github.com/Saksham4796/vm_for_se_problem) repo presents the code for creating instances and runnning the application on those instance in a distributed fashion.

The `docker_command.md` file contains all the relevant docker commands used in developing this application.
