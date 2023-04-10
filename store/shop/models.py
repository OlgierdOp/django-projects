from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    price = models.IntegerField(null=True)
    gender = models.CharField(choices=[("F", "Female"), ("M", "Male")], max_length=100)
    pic = models.ImageField(upload_to='shop/images/', null=True)

    def __str__(self): return f"{self.name}"





class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item)

    def total_cost(self):
        return sum(cart_item.item.price * cart_item.item.quantity for cart_item in self.cart_item_set.all())

    def __str__(self):
        return f"Cart: {self.user.username}"
