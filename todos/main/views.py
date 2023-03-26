# from django.http import HttpResponse
from django.shortcuts import render

from main.forms import ContactForm


# Create your views here.


def hello(request, name="World"):
    # return HttpResponse(f"Hello {name}!")
    return render(
        request=request,
        template_name="home.html",
        context={"name": name}
    )


def send_email(name, email, content):
    print(f"Wiadomośc od {name} ({email})")
    print(content)

def contact(request):

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        content = request.POST.get("content")

        send_email(name, email, content)

    form = ContactForm()



    return render(
        request,
        "contact.html",
        {"form": form}
    )