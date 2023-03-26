from django import forms


class NumberField(forms.Form):
    number_1 = forms.CharField(label="Number_1")
    number_2 = forms.CharField(label="Number_2")
