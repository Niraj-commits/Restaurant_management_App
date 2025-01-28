from django.urls import path,include
from .views import *

urlpatterns = [
    path("category_list",categoryList),
    path("category_list/<pk>",singleCategoryData),
    path("food_list",foodList),
    path("food_list/<pk>",singleFoodData),
    path("table_list",tableList),
    path("table_list/<pk>",singleTableData),
    path("order_list",orderList),
    path("order_list/<pk>",singleOrderData),
    path("order_item_list",orderItemList),
    path("order_item_list/<pk>",singleOrderItem),
]
