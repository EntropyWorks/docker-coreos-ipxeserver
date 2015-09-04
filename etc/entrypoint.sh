#!/usr/bin/env bash

if [ "$MODE" == "dev" ]; then
    python app.py
else
    gunicorn --config=gunicorn.py app:app
fi
