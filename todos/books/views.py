from django.conf import settings
from django.contrib import messages
from django.shortcuts import render

from books.forms import BookForm
from books.models import Book
from common.views import paginate


# Create your views here.

def book_list(request):

    page_obj = paginate(request, Book)

    if request.method == "POST":
        form = BookForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            # Book.objects.create(**form.cleaned_data)
            book = form.save()
            messages.success(request, f"Książka {book.title} została utworzona")

    form = BookForm()

    return render(
        request,
        "books/list.html",
        {"page_obj": page_obj, "form": form}
    )


def book_details(request, id):
    book = Book.objects.get(pk=id)
    if request.method == "POST":
        form = BookForm(instance=book, data=request.POST, files=request.FILES)
        if form.is_valid():
            # for field, value in form.cleaned_data.items():
            #     setattr(book, field, value)

            form.save()

    # form = BookForm(data=book.__dict__)
    form = BookForm(instance=book)

    return render(
        request,
        "books/details.html",
        {"book": book, "form": form}
    )


def handle_uploaded_file(f, path):
    with open(path, "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def upload_file(request):
    if request.method == "POST":
        name = settings.MEDIA_ROOT + "/books/images/xxx.jpg"
        f = request.FILES["upload_file"]
        handle_uploaded_file(f, name)

    return render(request, "books/cover_upload.html", {})
