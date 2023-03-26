from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

from books.models import Book


class BookForm_old(forms.Form):
    title = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    # author = forms.CharField()
    year = forms.IntegerField()

    helper = FormHelper()
    helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
    # helper.form_method = 'POST'


class BookForm(forms.ModelForm):
    # title = forms.CharField()
    # description = forms.CharField(widget=forms.Textarea)
    # author = forms.CharField()
    # year = forms.IntegerField()

    helper = FormHelper()
    helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))

    class Meta:
        model = Book
        fields = [
            "title",
            "description",
            "author",
            "year",
            "cover",
        ]
