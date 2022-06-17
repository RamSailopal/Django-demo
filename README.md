# Django-demo

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/RamSailopal/Django-demo)

A simple demo of the Python Django framework using mysql as a backend

Creates a simple api for adding users to a mysql table

Tables are created in mysql using the Django migrations framework https://docs.djangoproject.com/en/4.0/topics/migrations/

# Provisioning

    git clone https://github.com/RamSailopal/Django-demo.git
    cd Django-demo
    docker-compose up
    
# Backend
    
    
On completion of the provisioning of the environment, navigate to http://serveraddress:8000/test/users to GET and POST data

# Mysql view

     mysql> select * from newproject_api_users;
     +----+------+-----+-----+
     | id | name | age | sex |
     +----+------+-----+-----+
     |  1 | Ram  | 21  | M   |
     |  2 | Bob  | 52  | M   |
     +----+------+-----+-----+
     2 rows in set (0.00 sec)
     
# Creating a new project

To create a new project, run:

     django-admin startproject newproject
     cd newproject
     django-admin startapp new_api

The critical files are then:

**newproject_api/models.py** - Used to set up mysql  tables using migrations

**newproject_api/Serializers.py** - Converts table data into a JSON API format

**newproject_api/views.py** - Allows data to be viewed in a browser

**newproject_api/urls.py** - Connects endpoints to views

**newproject/urls.py** - Redirects the main project to the apis

**newproject/settings.py** - Which backend database to use, allowed hosts installed apps

# Front-end

A crude front-end to demonstate the use of Jinja templates has been added.

To view the front-end, navigate to:

http://serveraddress:8001

