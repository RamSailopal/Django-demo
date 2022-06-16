from django.urls import path, include

urlpatterns = [
   path('test/', include('newproject_api.urls')),
]
