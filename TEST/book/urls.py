from django.urls import path
from .views import add_book, delete_book, book_delete

urlpatterns = [
    path('books/', add_book, name='books'),
    path('delete_book/', delete_book, name='delete_book'),
    path('book_delete/', book_delete, name='book_delete')
]
