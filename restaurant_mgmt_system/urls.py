from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'category',category,basename="category")

urlpatterns = [
   
    # path("food_list",foodList),
    # path("food_list/<pk>",singleFoodData),
    # path("tables",tables.as_view()),
    # path("tables/<pk>",SingleTableListData.as_view()),
    # path("order_list",orderList),
    # path("order_list/<pk>",singleOrderData),
    # path("order_item_list",orderItemList.as_view()),
    # path("order_item_list/<pk>",singleOrderItem.as_view()),
    path('',include(router.urls)),
]