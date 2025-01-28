from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField()
    
    def create(self,validated_data):
        return Category.objects.create(**validated_data)
    
class FoodSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField()
    description = serializers.CharField()
    category = serializers.CharField()
    price = serializers.IntegerField()
    
    def create(self, validated_data):
        return Food.objects.create(**validated_data)
    

class TableSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField()
    is_available = serializers.BooleanField()
    
    def create(self, validated_data):
        return Table.objects.create(**validated_data)
    

class OrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    user = serializers.CharField()
    table_id = serializers.CharField()
    status = serializers.ChoiceField(choices=[('p','pending'),('a','accepted')] )
    quantity = serializers.IntegerField()
    
    def create(self, validated_data):
        return Order.objects.create(**validated_data)

class OrderItemsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    order = serializers.CharField()
    food = serializers.CharField()
    
    def create(self, validated_data):
        return OrderItem.objects.create(**validated_data)