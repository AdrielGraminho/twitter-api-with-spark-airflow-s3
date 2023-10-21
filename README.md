# Twitter API Data Extraction and Superset Dashboard

## Overview
This project aims to extract data from the Twitter API using Python, Airflow, and Spark, and provide a dashboard in Superset.

## Prerequisites
Make sure you have the following tools installed:
- Docker
- Docker Compose

## Environment Setup
To set up the environment, follow these steps:
1. Clone this repository.
2. Navigate to the root directory of the project.
3. Run the command `docker-compose up` to start the services.

Make sure to set up the Twitter API credentials before running the project.

## Application Ports
The application ports are as follows:
- Airflow: 8085
- Spark:
  - Spark Master Port: 8080
  - Spark Worker Port: 7077
  - Spark Web UI Port: 8081
- PostgreSQL: (Default Port: 5432)
- Redis: (Default Port: 6379)

## Project Structure
|- docker-compose.yml
|- README.md
|- dags/
|  |- utils/
|  |   | - conection_postgresql.py
|  |   | - conection_db_factory.py
|  |- twitter_extraction.py
