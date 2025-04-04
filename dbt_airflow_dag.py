from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

# Define the DAG
dag = DAG(
    'dbt_airflow_dag',  # Name of your DAG
    description='A simple DAG to run DBT models and validate completion',
    schedule_interval=timedelta(days=1),  # Run once every 24 hours
    start_date=datetime(2025, 3, 31),  # Start date of your DAG
    catchup=False,  # This prevents backfilling
)

# Define the tasks

# Task 1: Ingest the CSV into the PostgresDB (using a BashOperator for now)
ingest_csv_task = BashOperator(
    task_id='ingest_csv',
    bash_command="psql -h localhost -U postgres -d postgres -f /home/sanjana/airflow/dags/sample_utf8.csv",  # Replace with actual command
    dag=dag,
)

# Task 2: Trigger the DBT models
trigger_dbt_task = BashOperator(
    task_id='trigger_dbt',
    bash_command="dbt run --project-dir /home/sanjana/airflow/dags/my_dbt_project",  # Replace with actual DBT command
    dag=dag,
)

# Task 3: Validate DBT model completion (you can adjust this task based on your actual validation requirements)
validate_dbt_task = BashOperator(
    task_id='validate_dbt',
    bash_command="dbt run-operation validate_model_completion",  # Replace with actual validation command
    dag=dag,
)

# Set task dependencies
ingest_csv_task >> trigger_dbt_task >> validate_dbt_task
