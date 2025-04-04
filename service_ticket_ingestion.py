from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
import pandas as pd
import psycopg2

# Define default args
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define a function to ingest the CSV data into PostgresDB
def ingest_csv_to_postgres():
    # Database connection details
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="sanjana",
        port="5432"
    )
    cursor = conn.cursor()

    # Read CSV file (Update this path to your CSV file location)
    df = pd.read_csv('/home/sanjana/airflow/dags/sample_utf8.csv', na_values=["UNKNOWN"])
    df['inc_sla_due'] = pd.to_datetime(df['inc_sla_due'], errors='coerce')  # Convert to datetime
    df['inc_sys_created_on'] = pd.to_datetime(df['inc_sys_created_on'], errors='coerce')
    df['inc_resolved_at'] = pd.to_datetime(df['inc_resolved_at'], errors='coerce')

    df = df.where(pd.notnull(df), None)

    # Create table if not exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sample (
            inc_business_service VARCHAR(255),
            inc_category VARCHAR(255),
            inc_number VARCHAR(255),
            inc_priority VARCHAR(50),
            inc_sla_due TIMESTAMP,
            inc_sys_created_on TIMESTAMP,
            inc_resolved_at TIMESTAMP,
            inc_assigned_to VARCHAR(255),
            inc_state VARCHAR(255),
            inc_cmdb_ci VARCHAR(255),
            inc_caller_id VARCHAR(255),
            inc_short_description TEXT,
            inc_assignment_group VARCHAR(255),
            inc_close_code VARCHAR(255),
            inc_close_notes TEXT
        )
    """)
    conn.commit()

    # Insert data into PostgresDB
    for index, row in df.iterrows():
    	cursor.execute("""
        	INSERT INTO sample (
            		inc_business_service, inc_category, inc_number, inc_priority,
            		inc_sla_due, inc_sys_created_on, inc_resolved_at, inc_assigned_to,
            		inc_state, inc_cmdb_ci, inc_caller_id, inc_short_description,
            		inc_assignment_group, inc_close_code, inc_close_notes
        	) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    	""", (
        	row['inc_business_service'], row['inc_category'], row['inc_number'], row['inc_priority'],
        	None if pd.isna(row['inc_sla_due']) else row['inc_sla_due'],
        	None if pd.isna(row['inc_sys_created_on']) else row['inc_sys_created_on'],
        	None if pd.isna(row['inc_resolved_at']) else row['inc_resolved_at'],
        	row['inc_assigned_to'], row['inc_state'], row['inc_cmdb_ci'], row['inc_caller_id'],
        	row['inc_short_description'], row['inc_assignment_group'], row['inc_close_code'],
        	row['inc_close_notes']
    	))

    conn.commit()

    # Close connections
    cursor.close()
    conn.close()

# Define DAG
with DAG(
    'service_ticket_ingestion',
    default_args=default_args,
    description='Ingest CSV, run DBT models, and validate them',
    schedule_interval='@daily',
    start_date=datetime(2025, 3, 30),
    catchup=False,
) as dag:

    ingest_task = PythonOperator(
        task_id='ingest_csv_to_postgres',
        python_callable=ingest_csv_to_postgres
    )

    dbt_run_task = BashOperator(
        task_id='run_dbt_models',
        bash_command='cd /home/sanjana/airflow/dags/my_dbt_project && dbt run --profiles-dir /home/sanjana/airflow/dags/my_dbt_project'
    )

    dbt_validate_task = BashOperator(
        task_id='validate_dbt_run',
        bash_command='cd /home/sanjana/airflow/dags/my_dbt_project && dbt test --profiles-dir /home/sanjana/airflow/dags/my_dbt_project'
    )

    # Define task dependencies
    ingest_task >> dbt_run_task >> dbt_validate_task

