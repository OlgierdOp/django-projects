from django import forms


class ContactField(forms.Form):
    kontakt = forms.CharField(label="Contact")
    name = forms.CharField(label="Name")


