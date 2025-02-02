from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter
from debug_toolbar.toolbar import debug_toolbar_urls

router = DefaultRouter()
router.register(r'category',category,basename="category")

urlpatterns = [
    # path("category_list",categoryList.as_view({'get':'get'})), First = method name , second = func name
    # path("category_list/<pk>",singleCategoryData),
    path("food_list",foodList),
    path("food_list/<pk>",singleFoodData),
    path("tables",tables.as_view()),
    path("tables/<pk>",SingleTableListData.as_view()),
    path("order_list",orderList),
    path("order_list/<pk>",singleOrderData),
    path("order_item_list",orderItemList.as_view()),
    path("order_item_list/<pk>",singleOrderItem.as_view()),
    path('',include(router.urls)),
]+ debug_toolbar_urls()