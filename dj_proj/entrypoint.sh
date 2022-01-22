#! /bin/sh

python dj_proj/manage.py makemigrations

python dj_proj/manage.py migrate

cd ./dj_proj

exec gunicorn dj_proj.wsgi:application -b 0.0.0.0:8000 --reload