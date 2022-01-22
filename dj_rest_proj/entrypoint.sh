#! /bin/sh

python dj_rest_proj/manage.py makemigrations

python dj_rest_proj/manage.py migrate

cd ./dj_rest_proj

exec gunicorn dj_rest_proj.wsgi:application -b 0.0.0.0:8001 --reload