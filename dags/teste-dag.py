import airflow
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator
from pyspark.sql import SparkSession, functions

def teste_dag():
    print("start work")
    spark = SparkSession.builder \
    .appName('HelloWorld') \
    .config("spark.driver.maxResultSize", "8g") \
    .config("spark.network.timeout", 10000000) \
    .config("spark.executor.heartbeatInterval", 10000000) \
    .master("spark://spark:7077") \
    .getOrCreate()
    
    data = [("Hello",), ("World",)]
    df = spark.createDataFrame(data, ["Greeting"])
    
    df.show()
    
    spark.stop()
    
    
default_args = {
    'owner': 'adriel',
    'start_date': datetime(2023, 10, 22),
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