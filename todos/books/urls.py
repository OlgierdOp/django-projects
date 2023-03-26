from django.urls import path

from books.views import book_list, book_details, upload_file

app_name = "books"

urlpatterns = [
    path("", book_list, name='list'),
    path("<int:id>", book_details, name="details"),
    path("upload/", upload_file)
]