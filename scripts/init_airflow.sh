#!/bin/bash
set -e

echo "🚀 Initializing Airflow..."
echo ""

# Check if .env exists
if [ ! -f .env ]; then
    echo "❌ Error: .env file not found!"
    echo "Please copy .env.example to .env and configure it:"
    echo "  cp .env.example .env"
    echo "  # Then edit .env with your Snowflake credentials"
    exit 1
fi

# Load environment variables
set -a
source .env
set +a

# Create airflow_data directory if it doesn't exist
mkdir -p ${AIRFLOW_HOME}

echo "📦 Activating virtual environment..."
source .venv/bin/activate

echo "🗄️  Initializing Airflow database..."
airflow db init

echo "👤 Creating admin user..."
airflow users create \
    --username admin \
    --firstname Admin \
    --lastname User \
    --role Admin \
    --email admin@example.com \
    --password admin \
    2>/dev/null || echo "ℹ️  Admin user already exists"

echo ""
echo "✅ Airflow initialized successfully!"
echo ""
echo "📍 Database location: ${AIRFLOW_HOME}/airflow.db"
echo "📁 DAGs folder: ${AIRFLOW__CORE__DAGS_FOLDER}"
echo ""
echo "Next steps:"
echo "  ./scripts/start_airflow.sh"
