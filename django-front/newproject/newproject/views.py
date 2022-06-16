from django.http import HttpResponseRedirect
from django.shortcuts import render
import requests, json 
def home(request):
   r = requests.get('http://django-test:8000/test/users/?format=json')
   return render(request, 'home.html', {'users': r.json()})
def user(request, id):
   r = requests.get('http://django-test:8000/test/users/' + id  + '/?format=json')
   return render(request, 'user.html', {'user': r.json()})

