from django.contrib import admin
from import_export import resources

from common.admin import TagAdminHorizontal
from .models import Post
from import_export.admin import ExportMixin, ImportExportMixin


class PostResource(resources.ModelResource):
    class Meta:
        model = Post




# Register your models here.
@admin.register(Post)
class PostAdmin(ImportExportMixin, TagAdminHorizontal):
    readonly_fields = ("created", "modified")
    resource_class = PostResource
    autocomplete_fields = ("tags", )
