import pendulum
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import timedelta


default_args = {
    'owner': 'airflow',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}   
def my_python_function(age, ti):
        first_name = ti.xcom_pull(task_ids='get_name', key='first_name')
        last_name = ti.xcom_pull(task_ids='get_name', key='last_name')  
        print(f"Hello {first_name} {last_name}, you are {age}!")

def get_name(ti):
    ti.xcom_push(key='first_name', value="Emilio")
    ti.xcom_push(key='last_name', value="Momblant")

with DAG(
    dag_id='my_python_operator_dag_v4',
    default_args=default_args,
    description='A simple DAG with PythonOperator',
    start_date=pendulum.datetime(2021, 7, 29, 2, tz="UTC"),
    schedule='@daily',
    tags=['example', 'python_operator']
) as dag:
    task1 = PythonOperator(
        task_id='saludo',
        python_callable=my_python_function,
        op_kwargs={'age': 49}
    )
    task2 = PythonOperator(
        task_id='get_name',
        python_callable=get_name
    )   
    
    task2 >> task1