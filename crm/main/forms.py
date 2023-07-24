from django import forms
from .models import Order, Tag, MyUser


class OrderForm(forms.ModelForm):
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
