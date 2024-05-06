from airflow import DAG

from datetime import datetime



with DAG (
    'user_processing',
    start_date = datetime(2024, 1, 1),
    schedule = '@daily',
    catchup = False
) as dag:
    None