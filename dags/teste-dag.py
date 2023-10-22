import airflow
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator
from pyspark.sql import SparkSession, functions

def teste_dag():
    spark = SparkSession.builder \
    .appName('HelloWorld') \
    .master("spark://spark:7077") \
    .getOrCreate()
    
    data = [("Hello",), ("World",)]
    df = spark.createDataFrame(data, ["Greeting"])
    
    df.show()
    
    spark.stop()
    
    
default_args = {
    'owner': 'adriel',
    'start_date': datetime(2020, 11, 18),
    'retries': 10,
	  'retry_delay': timedelta(hours=1)
}
with airflow.DAG('dag_teste_spark',
                  default_args=default_args,
                  schedule_interval='0 1 * * *') as dag:
    task_elt_documento_pagar = PythonOperator(
        task_id='elt_documento_pagar_spark',
        python_callable=teste_dag
    )