from django.contrib import admin
from .models import *


# Register your models here.

class food(admin.ModelAdmin):
    list_display = ['name','description','category','price']
    list_editable = ['category','price']
    search_fields = ['name','category']
    list_filter = ['name']
    

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    
class order(admin.ModelAdmin):
    list_display = ['user','status','table_id','quantity']
    list_editable = ['status','quantity']
    search_fields = ['status','table_id']
    list_filter = ['status','table_id']
    inlines = [OrderItemInline]
    
class category(admin.ModelAdmin):
    list_display = ["id",'name']
    list_editable = ['name']
    search_fields = ['name']

class table(admin.ModelAdmin):
    list_display = ['id','number','is_available']
    list_editable = ['number','is_available']
    list_filter = ['is_available']
    search_fields = ['number']

admin.site.register(Food,food) #First order from model,second from admin
admin.site.register(OrderItem)
admin.site.register(Order,order)
admin.site.register(Category,category)
admin.site.register(Table,table)

