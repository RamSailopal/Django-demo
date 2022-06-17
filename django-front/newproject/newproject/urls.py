from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('user/<str:id>', views.user, name='user'),
    path('newuser/', views.newuser, name='newuser'),
    path('deluser/<str:id>', views.deluser, name='deluser'),
    path('amenduser/<str:id>', views.amenduser, name='amenduser'),
    path('updateuser/', views.updateuser, name='updateuser'),
]
