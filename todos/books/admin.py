from django.contrib import admin

from common.admin import TagAdminHorizontal
from .models import Book, Author, AuthorProfile
from import_export import resources
from import_export.admin import ExportMixin
class BookResource(resources.ModelResource):
    class Meta:
        model = Book

# Register your models here.

# class AuthorInline(admin.StackedInline):
#     model = Author

@admin.register(Book)
class BookAdmin(ExportMixin, TagAdminHorizontal):
    list_display = ["title", "author"]
    search_fields = ["title", "author", "description"]
    resource_class = BookResource

class AuthorProfileInline(admin.StackedInline):
    model = AuthorProfile


class BookInline(admin.TabularInline):
    model = Book
    extra = 1


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    inlines = [AuthorProfileInline, BookInline]

# @admin.register(AuthorProfile)
# class AuthorProfileAdmin(admin.ModelAdmin):
#     pass
