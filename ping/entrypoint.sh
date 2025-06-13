#!/bin/bash
echo "Waiting for database to be ready..."
sleep 20
echo "Database is ready, starting the application..."

exec gunicorn src.main:app \
  --workers 8 \
  --bind 0.0.0.0:8000 \
  --worker-class uvicorn.workers.UvicornWorker