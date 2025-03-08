from airflow import DAG 
from datetime import datetime
import os, sys
from airflow.operators.python import PythonOperator

plugins_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../plugins"))
sys.path.append(plugins_path)

from reddit_pipeline import reddit_pipeline
from aws_pipeline import aws_pipeline

default_args={
    'owner' : 'Sayam Khatri',
    'start_date' : datetime(2025, 3, 7)
}

file_postfix = datetime.now().strftime("%Y%m%d")

dag1 = DAG(
    dag_id='etl_reddit',
    default_args= default_args,
    schedule_interval='@daily',
    catchup=False
)

extract = PythonOperator(
    task_id = 'reddit_extraction',
    python_callable= reddit_pipeline,
    op_kwargs={
        'file_name' : f'reddit_{file_postfix}',
        'subreddit' : 'DataEngineering',
        'time_filter' : 'day',
        'limit' : 100
    },
    provide_context = True,
    dag = dag1
    
)

load = PythonOperator(
    task_id= 'load_to_s3',
    python_callable= aws_pipeline,
    provide_context = True,
    dag = dag1
)

extract >> load