from rest_framework import serializers

from newproject_api .models import Users 

class UsersSerializer(serializers.ModelSerializer):
   class Meta:
       model = Users
       fields = ('id', 'name', 'age', 'sex')

