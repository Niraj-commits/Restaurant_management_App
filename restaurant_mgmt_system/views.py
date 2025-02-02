from django.shortcuts import render,HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
from rest_framework import status,viewsets
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination

# using function views
  
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
    
@api_view(['GET','DELETE','PUT'])
def singleFoodData(request,pk):
    food_data = Food.objects.get(pk = pk) 
    if request.method == "GET":
        serializer = FoodSerializer(food_data)
        return Response(serializer.data)
    
    elif request.method == "DELETE":
        no_of_apperance = OrderItem.objects.filter(food = food_data).count() #checking for relation
        if no_of_apperance > 0:
            return Response({"details":"Data is used can't delete"},status=status.HTTP_404_NOT_FOUND)
        
        else:
            food_data.delete()
            return Response({"details":"Data has been deleted"},status=status.HTTP_200_OK)

    elif request.method == "PUT":
        serializer = FoodSerializer(food_data,data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"Details":"Data has been updated"},status=status.HTTP_200_OK)             
@api_view(['GET','POST'])
def orderList(request):
    if request.method == "GET":
        orders = Order.objects.all()
        serializer = OrderSerializer(orders,many = True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = OrderSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"Details":"Data Has been added"},status=status.HTTP_200_OK)

@api_view(['GET','DELETE','PUT'])
def singleOrderData(request,pk):
    order_data = Order.objects.get(pk = pk)
    if request.method == "GET":
        serializer = OrderSerializer(order_data)
        return Response(serializer.data)
    
    elif request.method == "DELETE":
        use_count = OrderItem.objects.filter(order = order_data).count()
        if use_count > 0 :
            return Response({"Details":"Cannot delete already using"},status=status.HTTP_226_IM_USED)
        
        else:
            order_data.delete()
            return Response({"Details":"Data has been deleted"},status=status.HTTP_200_OK)
        
    elif request.method == "PUT":
        serializer = OrderSerializer(order_data,data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"Details":"Details Have been updated"})
    
# Using ViewSets
# class category(viewsets.ViewSet):
#     def list(self,request):
#         queryset = Category.objects.all()
#         serializers = CategorySerializer(queryset,many= True)
#         return Response(serializers.data)
    
#     def retrieve(self,request,pk):
#         queryset = Category.objects.get(pk = pk)
#         serializer = CategorySerializer(queryset)
#         return Response(serializer.data)
        
#     def update(self,request,pk):
#         queryset = Category.objects.get(pk = pk)
#         serializer = CategorySerializer(queryset, data = request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"Details":"Data has been updated"},status=status.HTTP_200_OK)
    
#     def destroy(self,request,pk):
#         queryset = Category.objects.get(pk = pk)
        
#         total_usage = OrderItem.objects.filter(food__category = queryset).count()
        
#         if total_usage > 0 :
#             return Response({"Details":"Category is used"},status=status.HTTP_226_IM_USED)
        
#         else:
#             queryset.delete()
#             return Response({"Details":"Data is Deleted"},status=status.HTTP_200_OK)
        
#     def create(self,request):
#         serializer = CategorySerializer(data = request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)

# Using Generic API View
class tables(ListCreateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

class SingleTableListData(RetrieveUpdateDestroyAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    

# using class views

class orderItemList(APIView):
    
    def get(self,request):
        queryset = OrderItem.objects.all()
        serializer = OrderItemsSerializer(queryset,many = True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = OrderItemsSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"Details":"Data has been added"},status=status.HTTP_200_OK)
    

class singleOrderItem(APIView):
    
    def get(self,request,pk):
        queryset = OrderItem.objects.get(pk = pk)
        serializer = OrderItemsSerializer(queryset)
        return Response(serializer.data)

    def put(self,request,pk):
        queryset = OrderItem.objects.get(pk = pk)
        serializer = OrderItemsSerializer(queryset,data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"Details":"Data has been updated"},status=status.HTTP_200_OK)
    
    def delete(self,request,pk):
        queryset = OrderItem.objects.get(pk = pk)
        queryset.delete()
        return Response({"Details":"Data has been Deleted"})
    
class category(viewsets.ModelViewSet):
    
    # queryset = Category.objects.select_related(Category).all()
    queryset = Category.objects.all()
    
    serializer_class = CategorySerializer
    pagination_class = PageNumberPagination
    # def list(self,request):
    #     queryset = Category.objects.all()
    #     serializers = CategorySerializer(queryset,many= True)
    #     return Response(serializers.data)
    
    # def retrieve(self,request,pk):
    #     queryset = Category.objects.get(pk = pk)
    #     serializer = CategorySerializer(queryset)
    #     return Response(serializer.data)
        
    # def update(self,request,pk):
    #     queryset = Category.objects.get(pk = pk)
    #     serializer = CategorySerializer(queryset, data = request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response({"Details":"Data has been updated"},status=status.HTTP_200_OK)
    
    # def destroy(self,request,pk):
    #     queryset = Category.objects.get(pk = pk)
        
    #     total_usage = OrderItem.objects.filter(food__category = queryset).count()
        
    #     if total_usage > 0 :
    #         return Response({"Details":"Category is used"},status=status.HTTP_226_IM_USED)
        
    #     else:
    #         queryset.delete()
    #         return Response({"Details":"Data is Deleted"},status=status.HTTP_200_OK)
        
    # def create(self,request):
    #     serializer = CategorySerializer(data = request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)
