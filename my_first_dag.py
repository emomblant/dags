from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    "owner": "Emilio Momblant",
    "retries": 5,
    "retry_delay": timedelta(minutes=2)
}

with DAG(
    dag_id="our_first_dag",
    default_args=default_args,
    description="This is our first DAG by Emilio",
    schedule_interval="@daily",
    start_date=datetime(2021, 7, 29, 2),
    catchup=False,
) as dag:
    # Define your tasks here
    task1 = BashOperator(
        task_id="first_task",
        bash_command="echo Hello Airflow! I'm Emilio && sleep 5"
    )