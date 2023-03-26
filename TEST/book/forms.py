from django import forms
from .models import Book, Author


class BookForm(forms.ModelForm):
    author = forms.ModelChoiceField(queryset=Author.objects.all())

    class Meta:
        model = Book
        fields = ['title', 'description', 'author']


class BookDeleteForm(forms.Form):
    books_choice = forms.ModelChoiceField(queryset=Book.objects.all(), widget=forms.RadioSelect)
