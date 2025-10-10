#!/bin/bash
# start.sh
# Combined startup script for Render (backend + Streamlit)

echo "🚀 Installing dependencies..."
uv sync

echo "Starting FastAPI backend..."
uv run uvicorn app.main:app --host 0.0.0.0 --port 8000 &
BACKEND_PID=$!

echo "🌐 Waiting for backend to start..."
sleep 5

echo "💻 Starting Streamlit frontend..."
export BACKEND_URL="http://localhost:8000"
uv run streamlit run app/streamlit_app.py --server.port $PORT --server.address 0.0.0.0

wait $BACKEND_PID
