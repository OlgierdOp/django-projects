from django.contrib.auth.models import User
from django.db.models import Sum

from shop.models import Item, OrderItem, Order

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
