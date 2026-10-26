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
    dag_id="my_first_dag_v2",
    default_args=default_args,
    description="This is our first DAG by Emilio v2",
    start_date=pendulum.datetime(2021, 7, 29, 2, tz="UTC"),
    schedule="@daily",
    catchup=False,
    tags=["tutorial"],
) as dag:
    task1 = BashOperator(
        task_id="first_task",
        bash_command='echo "Hello Airflow! Task 1" && sleep 5',
    )

    task2 = BashOperator(
            task_id="second_task",
            bash_command='echo "Hello Airflow! Task 2" && sleep 5',
    )
    
    task3 = BashOperator(
            task_id="third_task",
            bash_command='echo "Hello Airflow! Task 3 at the same time than task2" && sleep 5',
    )
    task1.set_downstream(task2)
    task1.set_downstream(task3)