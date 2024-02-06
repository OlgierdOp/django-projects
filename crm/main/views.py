from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import OrderForm, SendToConstructorForm, OrderConstructorResponseForm, OrderClientResponseForm, \
    CustomUserCreationForm, \
    OrderResponseForm, MessageForm
from .models import Order, OrderResponseControl
from .my_scripts import check_user_group


@login_required(login_url="login_page")
def home(request):
    constructor_group = Group.objects.get(name='constructor')
    client_group = Group.objects.get(name='client')
    if request.method == "POST":
        order_form = OrderForm(request.POST, user=request.user)
        message_form = MessageForm(request.POST)
        del order_form.fields['customers']
        if order_form.is_valid() and message_form.is_valid():
            message = message_form.save()
            order = order_form.save(commit=False)
            order.message = message
            order.save()
            order.customers.set([request.user])
    else:
        order_form = OrderForm(user=request.user)
        message_form = MessageForm()
        if check_user_group(request.user, 'client'):
            del order_form.fields['customers']

    return render(request, "main/home.html", {
        "order_form": order_form,
        "message_form": message_form,
        'constructor_group': constructor_group,
        'client_group': client_group
    })


@login_required(login_url="login_page")
def order(request, id):

    user = request.user
    order = get_object_or_404(Order, id=id)
    order_message = order.message
    order_response = OrderResponseControl(order=order, user=user)

    client_order_form = None
    client_message_form = None
    constructor_message_form = None
    constructor_order_form = None

    if request.method == "POST":

        if check_user_group(user, 'client'):

            client_message_form = MessageForm(request.POST, instance=order_message)
            client_order_form = OrderClientResponseForm(request.POST, instance=order, user=user)

            if client_order_form.is_valid() and client_message_form.is_valid():

                client_order_form.save()
                client_message_form.save()
                order_response.save()
                order.customers.set([user])
                del client_order_form.fields['customers']
                return HttpResponse("SUCCESS")

        elif check_user_group(user, 'constructor'):

            constructor_message_form = MessageForm(request.POST, instance=order_message)
            constructor_order_form = OrderConstructorResponseForm(request.POST, instance=order)

            if constructor_order_form.is_valid() and constructor_message_form.is_valid():

                constructor_order_form.save()
                constructor_message_form.save()
                order_response.save()
                del constructor_order_form.fields['customers']

                return HttpResponse("SUCCESS")
    else:

        if check_user_group(user, 'client'):

            client_message_form = MessageForm(instance=order_message)
            client_order_form = OrderClientResponseForm(instance=order)
            del client_order_form.fields['customers']

        elif check_user_group(user, 'constructor'):

            constructor_message_form = MessageForm(instance=order_message)
            constructor_order_form = OrderResponseForm(instance=order)

        else:

            return HttpResponse("YOU ARE NOT PERMITTED TO VIEW THIS SITE")

    return render(request, 'main/orders.html ',
                  {'client_order_form': client_order_form,
                   'client_message_form': client_message_form,
                   "constructor_message_form": constructor_message_form,
                   'constructor_order_form': constructor_order_form
                   })


@login_required(login_url="login_page")
def admin(request):
    user = request.user
    admin_group = Group.objects.get(name='admin')
    orders = Order.objects.all()

    last_responses = {}
    for order in orders:
        last_response = OrderResponseControl.objects.filter(order=order).last()
        if last_response:
            last_responses[order.id] = last_response.user.username
        else:
            last_responses[order.id] = "Brak odpowiedzi"

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
        return render(request, 'main/admin_panel.html',
                      {"form": form, 'orders': orders, 'last_responses': last_responses})
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

            client_group = Group.objects.get(name='client')
            client_group.user_set.add(user)

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
def client_orders_panel(request):
    user = request.user
    orders = Order.objects.filter(customers=user)
    client_group = Group.objects.get(name='client')
    if client_group in user.groups.all():
        if request.method == "POST":
            pass
    else:
        return HttpResponse("You are not in the client group!")
    return render(request, 'main/client_messanger.html', {'orders': orders})
