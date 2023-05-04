from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    price = models.IntegerField(null=True)
    gender = models.CharField(choices=[("F", "Female"), ("M", "Male")], max_length=100)
    pic = models.ImageField(upload_to='shop/images/', null=True)
    tags = models.ManyToManyField('Tags')

    def __str__(self): return f"{self.name}"


class Tags(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item, through='CartItem')

    def total_cost(self):
        return sum(cart_item.item.price * cart_item.quantity for cart_item in self.cartitem_set.all())

    def __str__(self):
        return f"Cart: {self.user.username}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"Cart Item: {self.item.name} (Quantity: {self.quantity})"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    order_data = models.ForeignKey('OrderData', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.created_at}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"Item name: {self.item.name} Quantity: {self.quantity}"


class OrderData(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    delivery_address = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.IntegerField()
    postal_code = models.CharField(max_length=10)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

