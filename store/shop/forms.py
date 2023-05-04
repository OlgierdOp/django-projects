from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db.models import When, Case, Value, IntegerField

from .models import Item, OrderData, Tags


class ItemForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(queryset=Tags.objects.all())

    class Meta:
        model = Item
        fields = ['name', 'description', 'gender', 'price', 'pic', 'tags']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': "Username"}),
            'email': forms.EmailInput(attrs={'placeholder': "Email"}),

        }

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': "Password"})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': "Repeat Password"})


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['placeholder'] = "Username"
        self.fields['password'].widget.attrs['placeholder'] = "password"


class AddToCartForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, initial=1, label='Quantity')


class OrderDataForm(forms.ModelForm):
    class Meta:
        model = OrderData
        fields = ["name", 'last_name', 'delivery_address', 'email', 'phone_number', 'postal_code', "city", "country"
                  ]


class TagsForm(forms.Form):
    tags = forms.ModelMultipleChoiceField(queryset=Tags.objects.annotate(
        custom_order=Case(
            When(name="Men", then=Value(1)),
            When(name="Woman", then=Value(2)),
            default=Value(3),
            outputfield=IntegerField()
        )).order_by('custom_order', 'name'),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'tag-checkboxes'}))

