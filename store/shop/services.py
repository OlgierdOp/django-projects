from django.contrib.auth.models import User
from django.db.models import Sum

from shop.models import Item, OrderItem, Order


def item_counter():
    items = Item.objects.all()
    items_counter = 0
    for i in items:
        items_counter += 1
    return items_counter


def user_counter():
    users = User.objects.all()
    users_counter = 0
    for i in users:
        users_counter += 1
    return users_counter


def sold_item_counter():
    sold_item = OrderItem.objects.all()
    every_sold_item = sold_item.aggregate(total=Sum('quantity'))
    sold_items_counter = every_sold_item['total']
    return sold_items_counter


def sold_item_sum():
    orders = Order.objects.all()
    every_sold_item_price = orders.aggregate(total=Sum('total_cost'))
    total_cost = every_sold_item_price['total']
    return total_cost
