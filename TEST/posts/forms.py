from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title', 'content'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.form_action = ""


class CreateUserForm(UserCreationForm):
    helper = FormHelper()
    helper.add_input(Submit('submit', "Register", css_class="btn-success"))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class MessageForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea)
    user = forms.ModelChoiceField(queryset=User.objects.all())

    helper = FormHelper()
    helper.add_input(Submit('submit', "Send", css_class="btn-success"))
