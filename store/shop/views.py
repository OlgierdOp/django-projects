from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import CreateUserForm, CustomAuthenticationForm
from .forms import ItemForm, AddToCartForm
from .models import Item, Cart, CartItem


# Create your views here.
def home(request):
    form = ItemForm()
    items = Item.objects.all()
    admin_group = Group.objects.get(name="Admin")
    return render(request, 'shop/home_page_products.html', {'form': form, 'items': items, "admin_group": admin_group})


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
            user = form.save(commit=False)
            form.save()
            group = Group.objects.get(name="Customer")
            user.groups.add(group)
            return redirect('login_page')

    return render(request, 'shop/register_page.html', {'form': form})


@login_required(login_url='/login/')
def buy(request, id):
    item = Item.objects.get(id=id)
    form = AddToCartForm()
    if request.method == "POST":
        form = AddToCartForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            cart, created = Cart.objects.get_or_create(user=request.user)
            cart_item, created = CartItem.objects.get_or_create(cart=cart, item=item)
            cart_item.quantity += quantity
            cart_item.save()
            return redirect('cart')
    return render(request, "shop/buy.html", {'item': item, 'form': form})


@login_required(login_url="/login/")
def add_to_cart(request, id):
    item = Item.objects.get(id=id)
    cart, created = Cart.objects.get_or_create(user=request.user)

    try:
        cart_item = CartItem.objects.get(cart=cart, item=item)
        cart_item.quantity += 1
    except CartItem.DoesNotExist:
        cart_item = CartItem(cart=cart, item=item, quantity=1)
    cart_item.save()
    return redirect('home')


@login_required(login_url="/login/")
def cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.cartitem_set.all()

    total_cost = cart.total_cost()
    return render(request, 'shop/cart.html',
                  {'cart_items': cart_items, 'total_cost': total_cost})


@login_required(login_url="/login/")
def delete_item_from_cart(request, id):
    cart = get_object_or_404(Cart, user=request.user)
    item = get_object_or_404(Item, pk=id)
    cart_item = get_object_or_404(CartItem, cart=cart, item=item)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')


@login_required(login_url="/login/")
def admin_panel(request):
    user = request.user
    admin_group = Group.objects.get(name="Admin")

    if admin_group in user.groups.all():
        users = User.objects.all()
        counter = 0
        for i in users:
            counter += 1
        return render(request, "shop/admin_panel.html", {"counter": counter})

    else:
        return render(request, "shop/access_denied.html")
