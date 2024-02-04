from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class CustomUserManager(UserManager):
    pass


class MyUser(AbstractUser):
    def __str__(self):
        return f"{self.username}"


class Message(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=10000)

    def __str__(self):
        return f"{self.title}"


class File(models.Model):
    file = models.FileField(upload_to="uploads/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.file.name}"


class OrderResponseControl(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    response_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['response_date']

    def __str__(self):
        return f"{self.user} responded to {self.order} on {self.response_date}"


# OrderResponseControl enables to check who responded to order. Example last user that responded or first user


class Order(models.Model):
    customers = models.ManyToManyField(MyUser, related_name='customer_orders', blank=True, )
    constructor = models.ForeignKey(MyUser, on_delete=models.SET_NULL, null=True, blank=True,
                                    related_name='constructor_tasks')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, null=True)
    tag = models.ManyToManyField('Tag')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order: {self.message} date: {self.date}"


class Tag(models.Model):
    tag = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.tag}"
