from django.contrib import admin
from .models import OrderItem, CartItem, Invoice

# Register your models here.
admin.site.register(OrderItem)
admin.site.register(CartItem)
admin.site.register(Invoice)
