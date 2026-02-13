"""
Jaffle Shop dbt DAG using Cosmos.

This DAG uses Astronomer Cosmos to automatically create Airflow tasks
for each dbt model, providing better visualization and granular control.
"""

import os
from datetime import datetime
from pathlib import Path

from cosmos import DbtDag, ExecutionConfig, ProfileConfig, ProjectConfig
from cosmos.constants import ExecutionMode

# Get the project root directory
PROJECT_ROOT = Path(__file__).parent.parent
DBT_PROJECT_PATH = PROJECT_ROOT / "dbt"

# Configure Cosmos to use your existing profiles.yml
profile_config = ProfileConfig(
    profile_name="jaffle_shop",
    target_name="dev",
    profiles_yml_filepath=DBT_PROJECT_PATH / "profiles.yml",
)

# Configure dbt project - Cosmos will read dbt_project.yml automatically
project_config = ProjectConfig(
    dbt_project_path=DBT_PROJECT_PATH,
)

execution_config = ExecutionConfig(
    execution_mode=ExecutionMode.VIRTUALENV,
    virtualenv_dir=os.getenv("VIRTUAL_ENV", str(PROJECT_ROOT / ".venv")),
)

# Create the DAG using Cosmos
jaffleshop = DbtDag(
    project_config=project_config,
    profile_config=profile_config,
    execution_config=execution_config,
    dag_id="jaffleshop",
    start_date=datetime(2024, 1, 1),
    schedule="*/10 * * * *",
    catchup=False,
    default_args={
        "owner": "data_team",
        "retries": 0,
    },
    description="Jaffle Shop dbt pipeline with Cosmos visualization",
    tags=["dbt", "jaffleshop", "cosmos"],
)
