from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=25)
    
    def __str__(self):
        return self.name
    
class Food(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField( null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2,default=0.00,max_digits=500)
    
    def __str__(self):
        return self.name
    
    
class Table(models.Model):
    number = models.CharField(max_length=5)
    is_available = models.BooleanField(default=False)
    
    # def __str__(self):
    #     return self.number
    

class Order(models.Model):
    order_status = [('p','pending'),('c','confirmed')] 
    # or
    
    # PENDING = 'p'
    # COMPLETED = 'c'
    # order_status = {PENDING:'pending',COMPLETED:'completed'}
    
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    table_id = models.ForeignKey(Table,on_delete=models.CASCADE)
    status = models.CharField(max_length=25,choices=order_status,default='p')
    quantity = models.IntegerField(default=1)
    
    
class OrderItem(models.Model):
    
    order = models.ForeignKey(Order,on_delete=models.PROTECT)
    food = models.ForeignKey(Food,on_delete=models.PROTECT)
    
    
    # def __str__(self):
    #     return self.order
