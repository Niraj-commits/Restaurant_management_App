
from rest_framework import serializers

from django.contrib.auth import get_user_model

User = get_user_model()

class LoginSerializer(serializers.ModelSerializer):
     
     model = User
     fields = ["username","password"]