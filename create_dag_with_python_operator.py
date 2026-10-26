from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import timedelta

default_args = {
    'owner': 'airflow',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}   
def my_python_function():
        print("Hello from PythonOperator!")


with DAG(
    dag_id='my_python_operator_dag_v1',
    default_args=default_args,
    description='A simple DAG with PythonOperator',
    start_date=pendulum.datetime(2021, 7, 29, 2, tz="UTC"),
    schedule_interval='@daily',
    tags=['example', 'python_operator']
) as dag:
    task1 = PythonOperator(
        task_id='saludo',
        python_callable=my_python_function
    )   