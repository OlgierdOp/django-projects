from django.shortcuts import render
from .forms import ContactField
from .models import Contact


def contact(request):
    form = ContactField()
    if request.method == "POST":
        form = ContactField(request.POST)
        print(request.POST)
        if form.is_valid():
            kontakt_value = form.cleaned_data['kontakt']
            name_value = form.cleaned_data['name']
            print(f"{kontakt_value} {name_value}")

            data = Contact(contact=kontakt_value, name=name_value)
            data.save()
            return render(request, 'contact.html',
                          {
                              'form': form,
                              'kontakt_value': kontakt_value,
                              'name_value': name_value,
                          })
    else:
        return render(request, 'contact.html', {'form': form})
