from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import CreateUserForm, CustomAuthenticationForm
from .forms import ItemForm
from .models import Item, Cart


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
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/home")
    else:
        form = CustomAuthenticationForm()
    return render(request, 'shop/login_page.html', {'form': form})


def register_page(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_page')

    return render(request, 'shop/register_page.html', {'form': form})


@login_required(login_url='/login/')
def buy(request, id):
    item = Item.objects.get(id=id)
    return render(request, "shop/buy.html", {'item': item})


@login_required(login_url="/login/")
def add_to_cart(request, id):
    item = Item.objects.get(id=id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart.items.add(item)
    return redirect('home')


@login_required(login_url="/login/")
def cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = cart.items.all()
    total_cost = cart.total_cost()
    return render(request, 'shop/cart.html', {'items': items, 'total_cost': total_cost})


@login_required(login_url="/login/")
def delete_item_from_cart(request, id):
    cart = get_object_or_404(Cart, user=request.user)
    item = get_object_or_404(Item, pk=id)
    cart.items.remove(item)
    return redirect('cart')
