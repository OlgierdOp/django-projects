from django.contrib import admin
from .models import Todo
# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "done"]
    list_filter = ["done"]
    search_fields = ["title", "description"]

admin.site.register(Todo, TodoAdmin)


# @admin.register(Todo)
# class TodoAdmin(admin.ModelAdmin):
#     list_display = ["id", "title", "done"]
#     list_filter = ["done"]
#     search_fields = ["title", "description"]

