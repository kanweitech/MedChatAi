#!/bin/bash
echo "🚀 Starting Streamlit frontend..."
# Streamlit automatically uses $PORT from Render
streamlit run app/frontend/streamlit_app.py --server.port $PORT --server.address 0.0.0.0
