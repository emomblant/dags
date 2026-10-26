from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}   

with DAG(
    dag_id='my_python_operator_dag_v1',
    default_args=default_args,
    description='A simple DAG with PythonOperator',
    schedule_interval='@daily',
) as dag:

    def my_python_function():
        print("Hello from PythonOperator!")

    task1 = PythonOperator(
        task_id='saludo',
        python_callable=my_python_function
    )   