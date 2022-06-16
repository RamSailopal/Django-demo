#!/bin/bash
apt-get update
apt-get install -y python3 python3-pip
pip3 install -r /home/django/requirements.txt
cd /home/django/newproject
python3 manage.py runserver 0.0.0.0:8001
