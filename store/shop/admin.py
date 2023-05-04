from django.contrib import admin
from .models import Item, Cart, CartItem, OrderItem, Order, OrderData, Tags


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    pass


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderData)
class OrderDataAdmin(admin.ModelAdmin):
    pass
@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    pass
