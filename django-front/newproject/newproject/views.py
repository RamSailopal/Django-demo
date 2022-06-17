from django.http import HttpResponseRedirect
from django.shortcuts import render
import requests, json 
def home(request):
   r = requests.get('http://django-test:8000/test/users/?format=json')
   return render(request, 'home.html', {'users': r.json()})
def user(request, id):
   r = requests.get('http://django-test:8000/test/users/' + id  + '/?format=json')
   return render(request, 'user.html', {'user': r.json()})
def amenduser(request, id):
   r = requests.get('http://django-test:8000/test/users/' + id  + '/?format=json')
   return render(request, 'amenduser.html', {'user': r.json()})
def newuser(request):
   if request.method  == 'POST':
      name = request.POST.get("name")
      age = request.POST.get("age")
      sex = request.POST.get("sex")
      id = request.POST.get("id")
      jsonstr = { 'id': id,'name': name, 'age': age, 'sex': sex }
      x = requests.post('http://django-test:8000/test/users/', json = jsonstr)
      print(x.text)
      if "users with this id already exists" in x.text:
         return render(request, 'newusererror.html', {'id': id })
      else:
         r = requests.get('http://django-test:8000/test/users/?format=json')
         return render(request, 'home.html', {'users': r.json()})
   else:
      return render(request, 'newuser.html')
def deluser(request, id):
   if request.method  == 'GET':
      headers = {'content-type': 'application/json'}
      id=str(id)
      id=id.replace(" ","")
      print(id)
      r = requests.delete('http://django-test:8000/test/users/' + id  + '/')
      print(r.text)
      r = requests.get('http://django-test:8000/test/users/?format=json')
      return render(request, 'home.html', {'users': r.json()})
   else:
      r = requests.get('http://django-test:8000/test/users/?format=json')
      return render(request, 'home.html', {'users': r.json()})
def updateuser(request):
   if request.method  == 'POST':
      name = request.POST.get("name")
      age = request.POST.get("age")
      sex = request.POST.get("sex")
      id = request.POST.get("id")
      r = requests.delete('http://django-test:8000/test/users/' + id  + '/')
      jsonstr = { 'id': id,'name': name, 'age': age, 'sex': sex }
      x = requests.post('http://django-test:8000/test/users/', json = jsonstr)
      print(x.text)
      if "users with this id already exists" in x.text:
         return render(request, 'newusererror.html', {'id': id })
      else:
         r = requests.get('http://django-test:8000/test/users/?format=json')
         return render(request, 'home.html', {'users': r.json()})
   else:
      return render(request, 'newuser.html')


