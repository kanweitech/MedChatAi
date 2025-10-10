#!/bin/bash
set -e

echo "Starting MedChat AI app..."

# Render provides the $PORT variable automatically
# Run FastAPI backend on $PORT
uv run uvicorn app.main:app --host 0.0.0.0 --port $PORT


