## Airflow Jaffle Shop 🧇 Project

Jaffle Shop dbt pipelines orchestrated with Apache Airflow, using [Astronomer Cosmos](https://astronomer.github.io/astronomer-cosmos/) for seamless dbt integration.

### Features

- ✅ **dbt + Airflow Integration**: Each dbt model becomes an Airflow task
- ✅ **Local Development**: Self-contained setup with SQLite database
- ✅ **uv Package Manager**: Fast, modern Python dependency management
- ✅ **Cosmos Framework**: Automatic DAG generation from dbt project

### Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/getting-started/installation/) package manager
- Snowflake access with private key authentication

### Quick Start

#### 1. Set Up Environment

```bash
# Sync Python dependencies
uv sync

# Activate virtual environment
source .venv/bin/activate
```

#### 2. Configure Credentials

```bash
# Copy example environment file
cp .env.example .env

# Edit .env and add your Snowflake private key
# SNOWFLAKE_PRIVATE_KEY=<your-key-here>
```

#### 3. Initialize Airflow (First Time Only)

```bash
./scripts/init_airflow.sh
```

This will:
- Create local SQLite database in `airflow_data/`
- Set up Airflow metadata
- Create admin user (username: `admin`, password: `admin`)

#### 4. Start Airflow

```bash
./scripts/start_airflow.sh
```

This starts both the Airflow scheduler and webserver.

#### 5. Access Airflow UI

Open your browser to: **http://localhost:8080**

- Username: `admin`
- Password: `admin`

### Project Structure

```
airflow_jaffleshop/
├── dags/
│   └── jaffle_shop_dag.py      # Cosmos-based dbt DAG
├── dbt/                         # dbt project
│   ├── models/
│   ├── seeds/
│   ├── dbt_project.yml
│   └── profiles.yml
├── scripts/
│   ├── init_airflow.sh          # Initialize Airflow
│   └── start_airflow.sh         # Start Airflow services
├── airflow_data/                # Local Airflow database & logs (gitignored)
├── .env                         # Environment variables (gitignored)
├── .env.example                 # Template for environment variables
└── pyproject.toml               # Python dependencies
```

### Running dbt Directly (Optional)

You can still run dbt commands directly without Airflow:

```bash
cd dbt
dbt deps
dbt build
```

### Stopping Airflow

Press `Ctrl+C` in the terminal where `start_airflow.sh` is running.

### Troubleshooting

**Issue**: DAGs not showing up in UI
**Solution**: Check `airflow_data/logs/scheduler/` for errors

**Issue**: Database connection error
**Solution**: Verify your `.env` file has correct Snowflake credentials

**Issue**: Port 8080 already in use
**Solution**: Edit `scripts/start_airflow.sh` and change the port number

### Additional Resources

- [Astronomer Cosmos Documentation](https://astronomer.github.io/astronomer-cosmos/)
- [Apache Airflow Documentation](https://airflow.apache.org/docs/)
- [dbt Documentation](https://docs.getdbt.com/)
