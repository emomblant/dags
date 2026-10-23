from datetime import timedelta

import pendulum

from airflow.sdk import DAG
from airflow.providers.standard.operators.bash import BashOperator

default_args = {
    "owner": "Emilio Momblant",
    "retries": 2,
    "retry_delay": timedelta(minutes=2),
}

with DAG(
    dag_id="my_first_dag",
    default_args=default_args,
    description="This is our first DAG by Emilio",
    start_date=pendulum.datetime(2021, 7, 29, 2, tz="UTC"),
    schedule="@daily",
    catchup=False,
    tags=["tutorial"],
) as dag:
    task1 = BashOperator(
        task_id="first_task",
        bash_command='echo "Hello Airflow! I\'m Emilio" && sleep 5',
    )
