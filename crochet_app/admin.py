from django.contrib import admin

from .models import Creator
from .models import Technique
from .models import Product
from .models import Order
from .models import OrderProduct
from .models import Type

admin.site.register(Creator)
admin.site.register(Technique)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderProduct)
admin.site.register(Type)