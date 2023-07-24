from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import OrderForm, SendToConstructorForm
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

from .models import Order


@login_required(login_url="login_page")
def home(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.customer = request.user
            order.save()
    form = OrderForm()

    return render(request, "main/home.html", {"form": form})


def order(request, id):
    order = Order.objects.get(id=id)
    return render(request, 'main/orders.html ', {'order': order})


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
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)

                return redirect('/')
    form = AuthenticationForm()
    return render(request, "main/login.html", {'form': form})


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
