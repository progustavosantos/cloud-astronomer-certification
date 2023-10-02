from airflow import DAG 
from datetime import datetime

with DAG('my_dag', start_date=datetime(2022,1,1), schedule_interval='@daily', catchup=False) as dag:
    print('Hello World')        
