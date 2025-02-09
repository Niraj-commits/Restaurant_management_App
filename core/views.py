from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes
from .serializer import *
# using function views
  
  
@extend_schema(
    request = [LoginSerializer],
    methods = ['POST'],
    responses = {200:None})
# Create your views here.
class login(APIView):
    
    def post(self,request):
        username = request.data.get("username")
        password = request.data.get("password")
        
        if username == None and password == None:
            raise serializers.ValidationError({"Details":"username and password cannot be empty"})
        
        
        user = authenticate(username=username,password=password)
        if user:
          token,_ = Token.objects.get_or_create(user = user)
          return Response ({"token":token.key,"user":username})