from django.shortcuts import render,HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
from rest_framework import status

@api_view(['GET','POST'])
def categoryList(request):
    if request.method == "GET":
        list = Category.objects.all()
        serializer = CategorySerializer(list,many=True)
        return Response(serializer.data)
    
    
    elif request.method == "POST":
        serializer = CategorySerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response({"details":"Data Has Been Added"},status = status.HTTP_201_CREATED)
    
@api_view(['GET','DELETE'])    
def category_details(request,pk):
    single_category_data = Category.objects.get(pk = pk)
    if request.method == "GET":
        serializer = CategorySerializer(single_category_data)
        return Response(serializer.data)   
    
    else:
        datacount = Category.objects.filter(food__category = single_category_data).count() #check from orderitemmodel and then food model for connections
        
        if datacount > 0 :
            return Response({"details":"sorry the category is linked with other tables"},status= status.HTTP_404_NOT_FOUND)
        
        else:
            single_category_data.delete()
            return Response({"details":"Category Deleted"})
        
        
@api_view(['GET'])
def foodList(request):
    food_list = Food.objects.all()
    serializer = FoodSerializer(food_list,many = True)
    return Response(serializer.data)

@api_view(['GET'])
def tableList(request):
    table = Table.objects.all()
    serializer = TableSerializer(table,many = True)
    return Response(serializer.data)

@api_view(['GET'])
def orderList(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders,many = True)
    return Response(serializer.data)

@api_view(['GET'])

def orderItemList(request):
    orderItems = OrderItem.objects.all()
    serializer = OrderItemsSerializer(orderItems,many = True)
    
    return Response(serializer.data)




