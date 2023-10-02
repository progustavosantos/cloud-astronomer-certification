from airflow import DAG 
from datetime import datetime
from airflow.operators.python import PythonOperator

def _start():
    print('Hello World')

def _end():
    print('Goodbye World')



with DAG('my_dag', start_date=datetime(2022,1,1), schedule_interval='@daily', catchup=False) as dag:

    start = PythonOperator(
        task_id='start',
        python_callable=_start
    ) 

    end = PythonOperator(
        task_id='end',
        python_callable=_end
    ) 
    
    start >> end
     
