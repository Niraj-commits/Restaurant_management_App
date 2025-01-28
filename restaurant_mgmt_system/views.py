from django.shortcuts import render,HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics


@api_view(['GET','POST'])
def categoryList(request):
    if request.method == "GET":
        list = Category.objects.all()
        serializer = CategorySerializer(list,many=True)
        return Response(serializer.data)
    
    
    elif request.method == "POST":
        serializer = CategorySerializer(data = request.data) #deserializing for changing data into dict
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response({"details":"Data Has Been Added"},status = status.HTTP_201_CREATED)
    
@api_view(['GET','DELETE','PUT'])    
def singleCategoryData(request,pk):
    single_category_data = Category.objects.get(pk = pk)
    if request.method == "GET":
        serializer = CategorySerializer(single_category_data)
        return Response(serializer.data)   
    
    elif request.method == "DELETE":
        datacount = Category.objects.filter(food__category = single_category_data).count() #check from orderitemmodel and then food model for connections
        
        if datacount > 0 :
            return Response({"details":"sorry the category is linked with other tables"},status= status.HTTP_404_NOT_FOUND)
        
        else:
            single_category_data.delete()
            return Response({"details":"Category Deleted"})
    
    elif request.method == "PUT":
        
        serializer = CategorySerializer(single_category_data,data = request.data) #for updating we need instance
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"Details":"Data is updated"},status=status.HTTP_200_OK)
        
@api_view(['GET','POST'])
def foodList(request):
    
    if request.method == "GET":
        food_list = Food.objects.all()
        serializer = FoodSerializer(food_list,many = True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = FoodSerializer( data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"Details":"Data has been added"},status=status.HTTP_200_OK)
    
@api_view(['GET','DELETE'])
def singleFoodData(request,pk):
    food_data = Food.objects.get(pk = pk) 
    if request.method == "GET":
        serializer = FoodSerializer(food_data)
        return Response(serializer.data)
    
    else:
        no_of_apperance = OrderItem.objects.filter(food = food_data).count() #checking for relation
        if no_of_apperance > 0:
            return Response({"details":"Data is used can't delete"},status=status.HTTP_404_NOT_FOUND)
        
        else:
            food_data.delete()
            return Response({"details":"Data has been deleted"},status=status.HTTP_200_OK)

@api_view(['GET','POST'])
def tableList(request):
    if request.method == "GET":
        table = Table.objects.all()
        serializer = TableSerializer(table,many = True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = TableSerializer( data = serializer.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"details":"Data has been added"},status=status.HTTP_200_OK)

@api_view(['GET','DELETE'])
def singleTableData(request,pk):
    
    table_data = Table.objects.get(pk = pk)
    if request.method == "GET":
        serializer = TableSerializer(table_data)
        return Response(serializer.data)
    
    elif request.method == "DELETE":
        table_data.delete()
        return Response ({"Details":"Data has been deleted"},status=status.HTTP_404_NOT_FOUND) 

    
@api_view(['GET','POST'])
def orderList(request):
    if request.method == "GET":
        orders = Order.objects.all()
        serializer = OrderSerializer(orders,many = True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = OrderSerializer(data = serializer.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"Details":"Data Has been added"},status=status.HTTP_200_OK)

@api_view(['GET','DELETE'])
def singleOrderData(request,pk):
    order_data = Order.objects.get(pk = pk)
    if request.method == "GET":
        serializer = OrderSerializer(order_data)
        return Response({"Details":"Data Has been added"})
    
    elif request.method == "DELETE":
        use_count = OrderItem.objects.filter(order = order_data).count
        if use_count > 0 :
            return Response({"Details":"Cannot delete already using"},status=status.HTTP_226_IM_USED)
        
        else:
            order_data.delete()
            return Response({"Details":"Data has been deleted"},status=status.HTTP_200_OK)
        

@api_view(['GET','POST'])
def orderItemList(request):
    if request.method == "GET":
        orderItems = OrderItem.objects.all()
        serializer = OrderItemsSerializer(orderItems,many = True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = OrderItemsSerializer( data = serializer.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"Details":"Data is saved"},status=status.HTTP_200_OK)
    
@api_view(["GET","DELETE"])
def singleOrderItem(request,pk):
    
    orderItemData = OrderItem.objects.get(pk = pk)
    if request.method == "GET":
        serializer = OrderItemsSerializer(orderItemData)
        return Response(serializer.data)

    elif request.method == "DELETE":
        orderItemData.delete()
        return Response({"Details":"Data has been deleted"},status=status.HTTP_204_NO_CONTENT)



