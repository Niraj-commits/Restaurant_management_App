
from django_filters import rest_framework as filter
from .models import *

class customCategoryFilter(filter.FilterSet):
    class Meta:
        model = Category
        # fields = {
            # "name":["exact"],
            # "price":['gt','lt'],
            # 
        # }
        
        fields = ["name"]