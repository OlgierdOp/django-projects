from django.contrib import admin
from .models import UserProfile
from django.utils.safestring import mark_safe


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    readonly_fields = ["headshot_image"]

    fieldsets = (
        ("Główne", {
            'fields': ("user",
                       "description",
                       "headshot_image",
                       )
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('picture',),
        }),
    )


    def headshot_image(self, obj):
        return mark_safe('<img src="{url}" width="100" />'.format(
            url=obj.picture.url,
        ))
