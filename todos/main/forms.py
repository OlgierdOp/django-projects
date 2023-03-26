from django import forms

TOPICS = (("general", "General"), ("payments", "Payments"), ("technical", "Technical Problems"))
class ContactForm(forms.Form):
    name = forms.CharField(label="Imię")
    topis = forms.ChoiceField(choices=TOPICS)
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)