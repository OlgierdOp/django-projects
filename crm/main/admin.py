from django.contrib import admin

# Register your models here.
from main.models import Tag, Order, MyUser


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass
