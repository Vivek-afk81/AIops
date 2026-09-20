from datetime import datetime

from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator


def collect_metrics():
    cpu = 87
    memory = 65
    response_time = 420

    print("Metrics collected successfully")
    print("CPU:", cpu, "%")
    print("Memory:", memory, "%")
    print("Response Time:", response_time, "ms")


def process_metrics():
    print("Metrics processed successfully")


def detect_anomaly():
    cpu = 87

    if cpu > 80:
        print("Anomaly detected: High CPU usage")
    else:
        print("No anomaly detected")


def generate_report():
    print("===== AIOps Report =====")
    print("Metrics collected successfully")
    print("Metrics processed successfully")
    print("Anomaly detection completed")
    print("========================")


with DAG(
    dag_id="aiops_monitoring_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    collect = PythonOperator(
        task_id="collect_metrics",
        python_callable=collect_metrics,
    )

    process = PythonOperator(
        task_id="process_metrics",
        python_callable=process_metrics,
    )

    detect = PythonOperator(
        task_id="detect_anomaly",
        python_callable=detect_anomaly,
    )

    report = PythonOperator(
        task_id="generate_report",
        python_callable=generate_report,
    )

    collect >> process >> detect >> report
