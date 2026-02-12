#!/bin/bash
set -e

# Check if .env exists
if [ ! -f .env ]; then
    echo "❌ Error: .env file not found!"
    echo "Please copy .env.example to .env and configure it:"
    echo "  cp .env.example .env"
    exit 1
fi

# Load environment variables
set -a
source .env
set +a

# Check if Airflow is initialized
if [ ! -f "${AIRFLOW_HOME}/airflow.db" ]; then
    echo "❌ Error: Airflow not initialized!"
    echo "Please run: ./scripts/init_airflow.sh"
    exit 1
fi

# Activate virtual environment
source .venv/bin/activate

echo "🚀 Starting Airflow..."
echo ""
echo "📍 Airflow Home: ${AIRFLOW_HOME}"
echo "📁 DAGs Folder: ${AIRFLOW__CORE__DAGS_FOLDER}"
echo ""
echo "🌐 Access Airflow UI at: http://localhost:8080"
echo "   Username: admin"
echo "   Password: admin"
echo ""
echo "Press Ctrl+C to stop all services"
echo ""

# Trap to ensure both processes are killed on script exit
trap 'echo ""; echo "🛑 Stopping Airflow..."; kill $(jobs -p) 2>/dev/null; exit' INT TERM EXIT

# Start scheduler and webserver in background
airflow scheduler &
airflow webserver --port 8080 &

# Wait for both processes
wait
