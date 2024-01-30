from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from .models import Order, Tag, MyUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()


class OrderForm(forms.ModelForm):
    tag = forms.ModelMultipleChoiceField(queryset=Tag.objects.all())

    class Meta:
        model = Order
        fields = ['title', 'content', 'tag']


class OrderResponseForm(forms.ModelForm):
    tag = forms.ModelMultipleChoiceField(queryset=Tag.objects.all())

    class Meta:
        model = Order
        fields = ['title', 'content', 'tag']


class SendToConstructorForm(forms.Form):
    constructor = forms.ModelChoiceField(
        queryset=MyUser.objects.filter(groups__name='constructor')
    )
    orders = forms.ModelMultipleChoiceField(
        queryset=Order.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
