from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.contrib.admin.widgets import AutocompleteSelectMultiple
from django.contrib import admin
from posts.models import Post
from tags.models import Tag


class PostForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=AutocompleteSelectMultiple(
            Post._meta.get_field("tags"),
            admin.AdminSite()
        )
    )

    helper = FormHelper()
    helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))

    class Meta:
        model = Post
        fields = ["title", "content", "img", "datafile", "tags"]
