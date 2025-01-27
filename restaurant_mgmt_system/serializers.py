from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField()
    
    def create(self,validated_data):
        return Category.objects.create(**validated_data)
    
class FoodSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()
    category = serializers.CharField()
    price = serializers.IntegerField()
    

class TableSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    is_available = serializers.BooleanField()
    

class OrderSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    user = serializers.CharField()
    table_id = serializers.CharField()
    status = serializers.ChoiceField(choices=[('p','pending'),('a','accepted')] )
    quantity = serializers.IntegerField()

class OrderItemsSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    order = serializers.CharField()
    food = serializers.CharField()