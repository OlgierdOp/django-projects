from django.contrib import admin

class TagAdminHorizontal(admin.ModelAdmin):
    filter_horizontal = ["tags"]