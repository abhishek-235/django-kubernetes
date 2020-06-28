#!/bin/bash

# Collect static files
#echo "Collect static files"
#python manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
python ./myFirstProject/manage.py migrate

echo "Create superuser"
python ./myFirstProject/manage.py createadminuser

# Start server
echo "Starting server"
python ./myFirstProject/manage.py runserver 0.0.0.0:8000
#gunicorn --reload config.wsgi -c gunicorn.py -b 0.0.0.0:8888
