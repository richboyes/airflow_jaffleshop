"""
Jaffle Shop dbt DAG using Astronomer Cosmos.

This DAG automatically converts each dbt model into an Airflow task,
maintaining dependencies defined in dbt.
"""

from cosmos import DbtDag, ProjectConfig, ProfileConfig, ExecutionConfig
from datetime import datetime
from pathlib import Path

# Get the project root directory
PROJECT_ROOT = Path(__file__).parent.parent
DBT_PROJECT_PATH = PROJECT_ROOT / "dbt"

# Create the DAG using Cosmos
jaffle_shop_dag = DbtDag(
    # Project configuration
    project_config=ProjectConfig(
        dbt_project_path=str(DBT_PROJECT_PATH),
    ),
    # Profile configuration - reads from dbt/profiles.yml
    profile_config=ProfileConfig(
        profile_name="jaffle_shop",
        target_name="dev",
        profiles_yml_filepath=str(DBT_PROJECT_PATH / "profiles.yml"),
    ),
    # Execution configuration
    execution_config=ExecutionConfig(
        dbt_executable_path=str(PROJECT_ROOT / ".venv" / "bin" / "dbt"),
    ),
    # Operator arguments
    operator_args={
        "install_deps": True,  # Automatically run dbt deps
    },
    # DAG configuration
    schedule_interval="@daily",  # Change to None for manual trigger only
    start_date=datetime(2024, 1, 1),
    catchup=False,
    dag_id="jaffle_shop",
    default_args={
        "owner": "data_team",
        "retries": 2,
    },
)
