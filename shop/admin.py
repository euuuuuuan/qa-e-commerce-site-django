# shop/admin.py

from django.contrib import admin
from .models import Product, CartItem, Order, OrderItem # Order, OrderItem 추가

admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)