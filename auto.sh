#!/bin/bash


python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic --noinput
#python3 manage.py collectstatic
# sudo systemctl restart apache2
#sudo systemctl restart gunicorn
