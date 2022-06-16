#!/bin/bash
apt-get update
apt-get install -y python3 python3-pip  mysql-client libmysqlclient-dev
pip3 install -r /home/django/requirements.txt
mysql --user="root" --password="example" -h testmysql -e 'create database test;'
cd /home/django/newproject
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8000
