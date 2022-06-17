from django.db import models


class Users(models.Model):
       id  = models.CharField(max_length=100, primary_key=True)
       name = models.CharField(max_length=100)
       age  = models.CharField(max_length=3)
       sex  = models.CharField(max_length=1)


