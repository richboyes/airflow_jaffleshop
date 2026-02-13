## Airflow Jaffle Shop 🧇 Project

Jaffle Shop [dbt](https://www.getdbt.com/) pipelines orchestrated with [Apache Airflow](https://airflow.apache.org/) & [Cosmos](https://astronomer.github.io/astronomer-cosmos/).

### Prerequisites

- [uv](https://docs.astral.sh/uv/getting-started/installation/) package manager
- Snowflake access with private key authentication, stored to rsa_key.p8

### Quick Start

#### 1. Set Up Environment

```bash
# Sync Python dependencies
uv sync

# Activate virtual environment
source .venv/bin/activate
```

#### 2. Run Airflow

```bash
# Copy example environment file
cp .env.example .env

# Source environment variables and start Airflow
source .env
airflow standalone
```

#### 3. Access Airflow UI

Open your browser to: **http://localhost:8080**

See the generated credentials in `airflow/simple_auth_manager_passwords.json`

### Running dbt Directly (Optional)

You can still run dbt commands directly without Airflow:

```bash
uv sync
source .venv/bin/activate
source .env
cd dbt
dbt deps
dbt build
```

### Stopping Airflow

Press `Ctrl+C` in the terminal running `airflow standalone`

### Additional Resources

- [Apache Airflow Documentation](https://airflow.apache.org/docs/)
- [Astronomer Cosmos Documentation](https://astronomer.github.io/astronomer-cosmos/)
- [dbt Documentation](https://docs.getdbt.com/)
