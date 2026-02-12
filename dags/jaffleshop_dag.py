"""
Jaffle Shop dbt DAG.

This DAG runs dbt commands to build the Jaffle Shop data models.
"""

from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from datetime import datetime
from pathlib import Path
import os

# Get the project root directory
PROJECT_ROOT = Path(__file__).parent.parent
DBT_PROJECT_PATH = PROJECT_ROOT / "dbt"

default_args = {
    "owner": "data_team",
    "retries": 0,
}

with DAG(
    dag_id="jaffle_shop",
    default_args=default_args,
    description="Jaffle Shop dbt pipeline",
    schedule="*/10 * * * *",
    start_date=datetime(2024, 1, 1),
    catchup=False,
    is_paused_upon_creation=False,
    tags=["dbt", "jaffle_shop"],
) as dag:

    dbt_deps = BashOperator(
        task_id="dbt_deps",
        bash_command=f"cd {DBT_PROJECT_PATH} && dbt deps",
    )

    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command=f"cd {DBT_PROJECT_PATH} && dbt run",
    )

    dbt_test = BashOperator(
        task_id="dbt_test",
        bash_command=f"cd {DBT_PROJECT_PATH} && dbt test",
    )

    # Define task dependencies
    _ = dbt_deps >> dbt_run >> dbt_test
