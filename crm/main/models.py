from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

from crm import settings


class MyUser(AbstractUser):
    def __str__(self):
        return f"{self.username}"


class Order(models.Model):
    customer = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='customer_orders', null=True)
    constructor = models.ForeignKey(MyUser, on_delete=models.SET_NULL, null=True, blank=True,
                                    related_name='constructor_tasks')

    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    tag = models.ManyToManyField('Tag')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order: {self.title} date: {self.date}"


class Tag(models.Model):
    tag = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.tag}"
