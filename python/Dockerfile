FROM python:3.8

RUN mkdir /app
WORKDIR /app
COPY data_processing.py /app

# Copy requirements file to working directory
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt
