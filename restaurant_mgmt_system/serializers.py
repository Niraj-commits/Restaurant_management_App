from rest_framework import serializers
from .models import *
    
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
    
    vat_price = serializers.SerializerMethodField() #create new function to add extra data
    category = serializers.StringRelatedField() #to add name from a foreign table
    category_id = serializers.PrimaryKeyRelatedField(  #to add the id as well
        queryset = Category.objects.all(),
        source = "category"
        )

    class Meta:
        model = Food
        fields = ['id','name','description','category',"category_id",'price','vat_price']
    
    def get_vat_price(self,food:Food): #get is method and vat_price is declared variable
        return food.price *0.13 +food.price
        
    def create(self,validated_data):
        occurences = self.Meta.model.objects.filter(name = validated_data.get('name'),category = validated_data.get('category')).count()
        if occurences>0:
            raise serializers.ValidationError("Food already exist with that category")
        
        food = self.Meta.model(**validated_data)
        food.save()
        return food
    
    def update(self,instance,validated_data):
        occurences = self.Meta.model.objects.filter(name = validated_data.get('name'),category = validated_data.get('category')).count()

        if occurences > 0:
            raise serializers.ValidationError("Food already exist with that category")
        
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ['id','name','is_available']
        
    def create(self, validated_data):
        occurences = self.Meta.model.objects.filter(name = validated_data.get('name')).count()
        if occurences > 0:
            raise serializers.ValidationError("Same Named Table can't be created")
        
        table = self.Meta.model(**validated_data)
        table.save()
        return table
    
    def update(self,instance,validated_data):
        occurences = self.Meta.model.objects.filter(name = validated_data.get('name')).count()
        if occurences > 0:
            raise serializers.ValidationError("Same Named Table cannot be saved")
        
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance

class OrderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Order
        fields = ['id','user','table_id','status']
    
class OrderItemsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OrderItem
        fields = ['id',"order",'food','quantity']
        
    def create(self,validated_data):
        occurences = self.Meta.model.objects.filter(order = validated_data.get('order'),food = validated_data.get('food')).count()
        
        if occurences > 0:
            raise serializers.ValidationError("The item for that order is already added")
        
        item = self.Meta.model(**validated_data)
        item.save()
        return item
    
    def update(self,instance,validated_data):
        occurences = self.Meta.model.objects.filter(order = validated_data.get('order'),food = validated_data.get('food')).count()
        
        if occurences > 0:
            raise serializers.ValidationError("The item for that order is already added")
        
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance
    
    