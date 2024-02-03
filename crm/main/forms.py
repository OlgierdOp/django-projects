from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from .models import Order, Tag, MyUser, Message



class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()


class OrderForm(forms.ModelForm):
    tag = forms.ModelMultipleChoiceField(queryset=Tag.objects.all())
    customers = forms.ModelChoiceField(
        queryset=MyUser.objects.filter(groups__name='client')
    )

    class Meta:
        model = Order
        fields = ['tag']

    def __init__(self, *args, **kwargs):
        from main.my_scripts import check_user_group

        user = kwargs.pop('user', None)
        super(OrderForm, self).__init__(*args, **kwargs)
        if user and check_user_group(user, 'client'):
            self.fields['customers'].queryset = MyUser.objects.filter(pk=user.pk)
            self.fields['customers'].initial = user
            self.fields['customers'].required = False


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['title', 'content']


class OrderResponseForm(forms.ModelForm):
    tag = forms.ModelMultipleChoiceField(queryset=Tag.objects.all())
    customers = forms.ModelChoiceField(
        queryset=MyUser.objects.filter(groups__name='client')
    )
    class Meta:
        model = Order
        fields = ['tag', 'customers']

class SendToConstructorForm(forms.Form):
    constructor = forms.ModelChoiceField(
        queryset=MyUser.objects.filter(groups__name='constructor')
    )
    orders = forms.ModelMultipleChoiceField(
        queryset=Order.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
