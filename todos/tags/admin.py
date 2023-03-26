from django.contrib import admin
from .models import Tag
# Register your models here.

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ("name", )
    }
    search_fields = ("name", )