# ITSM Data Pipeline

## Overview
This project automates the extraction, transformation, and visualization of IT Service Management (ITSM) data using Apache Airflow, DBT, PostgreSQL, and Apache Superset. The pipeline processes raw ServiceNow ticket data, transforms it into meaningful insights, and presents it through interactive dashboards.

## Approach
1. **Data Ingestion:**  
   - ServiceNow ticket dump is loaded into PostgreSQL using Airflow.
   - The data is extracted in CSV format and loaded into a staging table.

2. **Data Transformation:**  
   - DBT (Data Build Tool) is used to clean, model, and aggregate the data.
   - Transformation steps include filtering, standardizing timestamps, and calculating key operational metrics.

3. **Data Visualization:**  
   - Apache Superset is connected to PostgreSQL.
   - Dashboards display key insights like ticket volume trends, resolution time, closure rates, and backlog.

## Assumptions
- The raw ServiceNow data is available in CSV format.
- PostgreSQL is used as the primary database for storing and transforming data.
- Airflow is scheduled to run ETL jobs periodically.
- Superset is used for dashboarding and requires proper database connections.


## Installation & Setup
1. **Clone the Repository**
   ```bash
   git clone https://github.com/sanjana1210/itsm-data-pipeline.git
   cd itsm-data-pipeline

2. **Set Up PostgreSQL**
   -sudo apt update
   -sudo apt install postgresql
   -sudo -u postgres psql
   -CREATE DATABASE itsm_db;

3. **Install Apache Airflow**
   pip install apache-airflow
   airflow db init
   airflow webserver & airflow scheduler

4. **Configure DBT**
   pip install dbt-postgres
   cd dbt
   dbt run

5. **Set Up Apache Superset**
   pip install apache-superset
   superset db upgrade
   superset init
   superset run -p 8088 --debugger --reload

6. **Load Data & Trigger Pipeline**

Upload the sample ServiceNow CSV into PostgreSQL.

Run the Airflow DAG (dbt_airflow_dag.py) to trigger transformations.

Access the Superset dashboard to analyze insights.





