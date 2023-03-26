from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    price = models.IntegerField(null=True)
    gender = models.CharField(choices=[("F", "Female"), ("M", "Male")], max_length=100)
    pic = models.ImageField(upload_to='shop/images/', null=True)

    def __str__(self): return f"{self.name}"
