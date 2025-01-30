from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'category',category,basename="category")

urlpatterns = [
    # path("category_list",categoryList.as_view({'get':'get'})), First = method name , second = func name
    # path("category_list/<pk>",singleCategoryData),
    path("food_list",foodList),
    path("food_list/<pk>",singleFoodData),
    path("table_list",tableList),
    path("table_list/<pk>",singleTableData),
    path("order_list",orderList),
    path("order_list/<pk>",singleOrderData),
    path("order_item_list",orderItemList),
    path("order_item_list/<pk>",singleOrderItem),
    path('',include(router.urls)),
]