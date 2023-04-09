from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import timedelta

with DAG(
    dag_id= 'docker_test_dag',
    description='Testing the docker operator',
    schedule_interval=None,
    start_date=days_ago(2),
    catchup=False,
    tags=['docker_test'],
    default_args={
        'owner': 'airflow',
        'email': ['airflow@example.com'],
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 0,
        'depends_on_past': False,
        'retry_delay': timedelta(minutes=5)
    }
) as dag:

    docker_test_task = DockerOperator(
        task_id='docker_test_task',
        image='docker-test-image',
        api_version='auto',
        auto_remove=True,
        mount_tmp_dir=False,
        container_name='docker-test-container',
        command='echo "this is a test message shown from within the container',
        docker_url='unix://var/run/docker.sock',
        network_mode='bridge'
    )

    docker_test_task