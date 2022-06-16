# Django-demo

A simple demo of the Python Django framework using mysql as a backend

Creates a simple api for adding users to a mysql table

Tables are created in mysql using the Django migrations framework https://docs.djangoproject.com/en/4.0/topics/migrations/

# Provisioning

    git clone https://github.com/RamSailopal/Django-demo.git
    cd Django-demo
    docker-compose up
    
    
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
