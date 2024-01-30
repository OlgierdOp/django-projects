from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import OrderForm, SendToConstructorForm, CustomUserCreationForm, OrderResponseForm
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import Order


@login_required(login_url="login_page")
def home(request):
    constructor_group = Group.objects.get(name='constructor')
    client_group = Group.objects.get(name='client')
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.customer = request.user
            order.save()
    form = OrderForm()

    return render(request, "main/home.html",
                  {"form": form, 'constructor_group': constructor_group, 'client_group': client_group})


@login_required(login_url="login_page")
def order(request, id):
    user = request.user
    client_group = Group.objects.get(name='client')
    order = get_object_or_404(Order, id=id)
    if request.method == "POST":
        form = OrderResponseForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
    else:
        if client_group in user.groups.all():
            form = OrderResponseForm(instance=order)
        else:
            return HttpResponse("YOU ARE NOT PERMITTED TO VIEW THIS SITE")
    return render(request, 'main/orders.html ', {'order': order, 'form': form})


@login_required(login_url="login_page")
def admin(request):
    user = request.user
    admin_group = Group.objects.get(name='admin')
    orders = Order.objects.all()
    if admin_group in user.groups.all():
        if request.method == "POST":
            form = SendToConstructorForm(request.POST)
            if form.is_valid():
                constructor = form.cleaned_data['constructor']
                orders = form.cleaned_data['orders']
                for order in orders:
                    order.constructor = constructor
                    order.save()
                return redirect('admin_panel')
        else:
            form = SendToConstructorForm()
        return render(request, 'main/admin_panel.html', {"form": form, 'orders': orders})
    else:
        return HttpResponse("You are not permitted to view this site")


def login_page(request):
    constructor_group = Group.objects.get(name='constructor')
    admin_group = Group.objects.get(name='admin')
    client_group = Group.objects.get(name='client')
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if admin_group in user.groups.all():
                    return redirect('admin_panel')
                elif client_group in user.groups.all():
                    return redirect('/')
                elif constructor_group in user.groups.all():
                    return redirect('constructor_panel')
    return render(request, "main/login.html", {'form': form})


@login_required(login_url="login_page")
def send_to_constructor(request, order_id):
    order = Order.objects.get(id=order_id)
    if request.method == "POST":
        form = SendToConstructorForm(request.POST)
        if form.is_valid():
            constructor = form.cleaned_data['constructor']
            order.constructor = constructor
            order.save()
            return redirect('/')
    form = SendToConstructorForm()
    return render(request, 'main/admin_panel.html', {"form": form})


def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = CustomUserCreationForm()
    return render(request, 'main/register.html', {'form': form})


@login_required(login_url="login_page")
def constructor_panel_view(request):
    user = request.user
    constructor_group = Group.objects.get(name='constructor')
    orders = Order.objects.filter(constructor=user)
    if constructor_group in user.groups.all():
        if request.method == "POST":
            pass
    else:
        return HttpResponse("You are not permitted to view this site")
    return render(request, 'main/constructor_panel.html', {'orders': orders})


@login_required(login_url="login_page")
def client_messanger_view(request):
    user = request.user
    orders = Order.objects.filter(customer=user)
    client_group = Group.objects.get(name='client')
    if client_group in user.groups.all():
        if request.method == "POST":
            pass
    else:
        return HttpResponse("You are not in the client group!")
    return render(request, 'main/client_messanger.html', {'orders': orders})
