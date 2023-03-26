from django.shortcuts import render, redirect
from .forms import BookForm, BookDeleteForm
from .models import Book


def add_book(request):
    books = Book.objects.all()
    form = BookForm()
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    return render(request, 'base1.html', {'books': books, 'form': form})


def delete_book(request):
    book = Book.objects.first()
    if book:
        book.delete()
    return redirect('books')


def book_delete(request):
    if request.method == "POST":

        form1 = BookDeleteForm(request.POST or None)
        if form1.is_valid():
            books_choice_value = form1.cleaned_data['books_choice']
            books_choice_value.delete()
            return redirect('books')
    else:
        form1 = BookDeleteForm()
    return render(request, 'book/book_forms.html', {'form1': form1})
