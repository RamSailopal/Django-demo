from rest_framework import viewsets

from newproject_api.serializers import UsersSerializer
from newproject_api.models import Users 


class UsersViewSet(viewsets.ModelViewSet):
   queryset = Users.objects.all()
   serializer_class = UsersSerializer

