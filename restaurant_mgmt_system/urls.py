from django.urls import path,include
from .views import *

urlpatterns = [
    path("category_list",categoryList),
    path("category_detail/<pk>",category_details),
    path("food_list",foodList),
    path("table_list",tableList),
    path("order_list",orderList),
    path("order_item_list",orderItemList),
]
