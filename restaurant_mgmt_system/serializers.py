from rest_framework import serializers
from .models import *


# class CategorySerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only = True)
#     name = serializers.CharField()
    
#     def create(self,validated_data):
#         return Category.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name',instance.name)
#         instance.save()
#         return instance
    
# Using Model Serializers Can use ModelSerializer instead for the code above
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name'] 
        # also can be defined using
        # fields = '__all__'
        
    
class FoodSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField()
    description = serializers.CharField()
    category = serializers.PrimaryKeyRelatedField(queryset = Category.objects.all())
    price = serializers.IntegerField()
    
    def create(self, validated_data):
        return Food.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.description = validated_data.get('description',instance.description)
        instance.category = validated_data.get('category',instance.category)
        instance.price = validated_data.get('price',instance.price)
        instance.save()
        return instance
    

class TableSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField()
    is_available = serializers.BooleanField()
    
    def create(self, validated_data):
        return Table.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        
        instance.name = validated_data.get('name',instance.name)
        instance.is_available = validated_data.get('is_available',instance.is_available)
        instance.save()
        return instance
    

class OrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    user = serializers.PrimaryKeyRelatedField(read_only = True)
    table_id = serializers.PrimaryKeyRelatedField(read_only = True)
    status = serializers.ChoiceField(choices=[('p','pending'),('a','accepted')] )
    quantity = serializers.IntegerField()
    
    def create(self, validated_data):
        return Order.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        
        instance.user = validated_data.get("user",instance.user)
        instance.table_id = validated_data.get("table_id",instance.table_id)
        instance.status = validated_data.get("status",instance.status)
        instance.quantity = validated_data.get("quantity",instance.quantity)
        instance.save()
        return instance

class OrderItemsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    order = serializers.PrimaryKeyRelatedField(queryset = Order.objects.all())
    food = serializers.PrimaryKeyRelatedField(queryset = Food.objects.all())
    
    def create(self, validated_data):
        return OrderItem.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        
        instance.order = validated_data.get("order",instance.order)
        instance.food = validated_data.get("food",instance.food)
        
        instance.save()
        return instance