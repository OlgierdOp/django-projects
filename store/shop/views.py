from django.shortcuts import render, redirect
from .forms import ItemForm
from .models import Item
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import CreateUserForm


# Create your views here.
def home(request):
    form = ItemForm()
    items = Item.objects.all()

    return render(request, 'shop/home_page_products.html', {'form': form, 'items': items})


def men_page(request):
    items = Item.objects.filter(gender="M")
    return render(request, 'shop/men_products.html', {'items': items})


def woman_page(request):
    items = Item.objects.filter(gender="F")
    return render(request, 'shop/woman_products.html', {'items': items})


def main_page(request):
    return render(request, 'shop/main_page.html')


def login_page(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/home")
    else:
        form = AuthenticationForm()
    return render(request, 'shop/login_page.html', {'form': form})


def register_page(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_page')

    return render(request, 'shop/register_page.html', {'form': form})
