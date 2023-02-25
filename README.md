# se_problem_statement

This repository holds a problem statement prominent in the software industry. The problem statement has been generated using a generative model called chatGPT. The software application satisfying the requirements of the given problem statement has also been developed using chatGPT.

The `sales_data_sample.csv` file contains the sample sales data for the problem statement and is uploaded to the MySQL database. The `Dockerfile` is used to build the docker image which contains the Sales data hosted on MySQL database. The `scripts` folder contains .sql files which can build the database on the docker container. The `docker-compose.yml` file creates the docker container using the image which was build using `Dockerfile`.

The `data_processing.py` file performs data processing operation on the dataset and thus stores total sale for each commodity for each month of the year in the `total_sales.csv` file.

This distributed application is executed on virtual machine intances present on google cloud platform. [VM Instance](https://github.com/Saksham4796/vm_for_se_problem) repo presents the code for creating instances and runnning the application on those instance in a distributed fashion.

The `docker_command.md` file contains all the relevant docker commands used in developing this application.
