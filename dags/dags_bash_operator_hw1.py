from airflow import DAG
import pendulum
from airflow.operators.bash import BashOperator

my_dag = DAG(   
    dag_id="dags_bash_operator_hw1",
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    catchup=False,
    tags=["homework"]
    
)


bash_t1 = BashOperator(
    task_id="bash_t1",
    bash_command="echo whoami",
    dag=my_dag
)

bash_t2 = BashOperator(
    task_id="bash_t2",
    bash_command="echo $HOSTNAME",
    dag=my_dag
)

bash_t1 >> bash_t2