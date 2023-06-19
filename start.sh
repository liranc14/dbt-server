#!/bin/sh
dbt docs generate && dbt docs serve &
gunicorn -c gunicorn.py app:app