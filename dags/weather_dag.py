"""
DAG (Directed Acyclic Graph) definition for the Weather ETL Pipeline.
This script configures the scheduling, retries, and orchestration
logic for the daily ingestion of Bogota's weather data.
"""

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

# Import the main orchestration function from the ETL modules
from main import run_etl

# Default arguments applied to all tasks within this DAG
default_args = {
    'owner': 'salim',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_entry': False,
    'retries': 1, # Number of times the task will attempt to restart if it fails
    'retry_delay': timedelta(minutes=5), # Wait time between retry attempts
}

# Define the DAG context
with DAG(
    dag_id='etl_weather_bogota_v1',
    default_args=default_args,
    description='Automated Daily ETL Pipeline for weather metrics in Bogota',
    start_date=datetime(2024, 1, 1),
    schedule_interval='@daily', #Cron-based or preset frequency (Once a day)
    catchup=False, #Do not run historical dates before the current date
    tags=['weather', 'etl', 'bogota']
) as dag:

    # Define the PythonOperator task
    #This task acts as a 'wrapper' that tells Airflow to execute our Python function
    task_etl = PythonOperator(
        task_id='run_full_pipeline',
        python_callable=run_etl
    )

    # Dependency definition
    # Since we have only one task, we simply list it.
    # If we had multiple, we would use '>>' to define the execution order.
    task_etl