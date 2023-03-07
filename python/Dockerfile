FROM ubuntu:22.04

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive \
    apt-get -y install default-jre-headless && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN export JAVA_HOME="$(dirname $(dirname $(readlink -f $(which java))))"

RUN apt-get update && \
	apt-get install -y wget

   
# Download Spark and set environment variables
RUN mkdir -p /opt/spark && \
	cd /opt/spark && \
	wget https://dlcdn.apache.org/spark/spark-3.3.2/spark-3.3.2-bin-hadoop3.tgz && \
	tar xvf spark-3.3.2-bin-hadoop3.tgz 

ENV SPARK_HOME /opt/spark/spark-3.3.2-bin-hadoop3
ENV PATH $PATH:$SPARK_HOME/bin

#RUN cd /

#RUN apt-get install -y python3.8
#RUN apt-get autoclean && \
#	apt-get clean && \
#	apt-get update && \
#	apt-get install python3.8 -y

RUN apt-get update && \
    apt-get install -y build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev && \
    wget https://www.python.org/ftp/python/3.10.9/Python-3.10.9.tgz && \
    tar -xf Python-3.10.*.tgz && \
    cd Python-3.10.*/ && \
    ./configure --enable-optimizations && \
    make -j $(nproc) && \
    make altinstall

ENV PYSPARK_PYTHON /usr/local/bin/python3.10

RUN mkdir /app
WORKDIR /app

# Install PySpark
RUN pip3.10 install pyspark

# Copy the data_processing_spark.py file to the working directory
COPY data_processing_spark.py /app
COPY output_HTML.py /app
COPY website.js /app

# Copy requirements file to working directory
COPY requirements.txt .

# Install dependencies
RUN pip3.10 install -r requirements.txt
