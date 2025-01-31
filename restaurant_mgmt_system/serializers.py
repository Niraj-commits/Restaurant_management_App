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
        
    def create(self,validated_data):
        occurences = self.Meta.model.objects.filter(name = validated_data.get('name')).count()
        if occurences > 0:
            raise serializers.ValidationError("Category Already Exist")
        
        category = self.Meta.model(**validated_data)
        category.save()
        return category 
        
    def update(self,instance,validated_data):
        occurences = self.Meta.model.objects.filter(name = validated_data.get('name')).count()
        
        if occurences > 0:
            raise serializers.ValidationError("Category Already Exist")
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance
            
    
class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['id','name','description','category','price']
        
        def save(self,**kwargs):
            validated_data = self.validated_data
            occurences = self.Meta.model.objects.filter(name =validated_data.get('name')).count()
    

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