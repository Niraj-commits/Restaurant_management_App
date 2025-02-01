from django.contrib import admin
from .models import *


# Register your models here.

class food(admin.ModelAdmin):
    list_display = ['name','description','category','price']
    list_editable = ['category','price']
    search_fields = ['name','category']
    list_filter = ['category']
    list_per_page = 15
    

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    
class order(admin.ModelAdmin):
    list_display = ['user','status','table_id']
    list_editable = ['status']
    search_fields = ['status','table_id']
    list_filter = ['status','table_id']
    inlines = [OrderItemInline]
    
class category(admin.ModelAdmin):
    list_display = ["id",'name']
    list_editable = ['name']
    search_fields = ['name']
    list_per_page = 10

class table(admin.ModelAdmin):
    list_display = ['id','name','is_available']
    list_editable = ['name','is_available']
    list_filter = ['is_available']
    search_fields = ['name']
    list_per_page = 10

admin.site.register(Food,food) #First order from model,second from admin
admin.site.register(OrderItem)
admin.site.register(Order,order)
admin.site.register(Category,category)
admin.site.register(Table,table)

