from django.urls import path, include
from rest_framework import routers
from newproject_api.views import UsersViewSet

router = routers.DefaultRouter()
router.register(r'users', UsersViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
