from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .forms import CreateUserForm, CustomAuthenticationForm, OrderDataForm
from .forms import ItemForm, AddToCartForm, TagsForm
from .models import Item, Cart, CartItem, Order, OrderItem, Tags
from .services import item_counter, user_counter, sold_item_counter, sold_item_sum


# Create your views here.
def home(request):
    form = ItemForm()
    items = Item.objects.all()
    admin_group = Group.objects.get(name="Admin")
    if request.method == "POST":
        tags_form = TagsForm(request.POST)
        if tags_form.is_valid():
            selected_tags = tags_form.cleaned_data["tags"]
            tag_names = ','.join(tag.name for tag in selected_tags)
            return redirect(reverse('filtered_item', kwargs={'tag_names': tag_names}))
    else:
        tags_form = TagsForm()
        return render(request, 'shop/home_page_products.html',
                      {'form': form, 'items': items, "admin_group": admin_group, "tags_form": tags_form})


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
            if not created:
                cart_item.quantity += quantity
            else:
                cart_item.quantity = quantity
            cart_item.save()
            return redirect('cart')
    return render(request, "shop/buy.html", {'item': item, 'form': form})


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

    if request.method == "POST":
        form = ItemForm(request.POST)
        form.save()
    else:
        if admin_group in user.groups.all():
            form = ItemForm()
            users_number = user_counter()
            items_number = item_counter()
            sold_items_number = sold_item_counter()
            sold_items_sum = sold_item_sum()

            return render(request, "shop/admin_panel.html",
                          {"users_number": users_number, "items_number": items_number,
                           "sold_items_number": sold_items_number, "sold_items_sum": sold_items_sum, "form": form})

        else:

            return render(request, "shop/access_denied.html")


@login_required(login_url="/login/")
def checkout(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.cartitem_set.all()
    total_cost = cart.total_cost()
    if request.method == "POST":

        order = Order(user=request.user, total_cost=total_cost)
        form = OrderDataForm(request.POST)
        order.save()
        form.save()
        for cart_item in cart_items:
            order_item = OrderItem(order=order, item=cart_item.item, quantity=cart_item.quantity)
            order_item.save()
            cart_item.delete()
        return redirect("order_success")
    else:
        form = OrderDataForm()
        return render(request, "shop/checkout.html", {"cart_items": cart_items, "cart": cart, "form": form})


@login_required(login_url="/login/")
def order_success(request):
    user_order = Order.objects.filter(user=request.user).last()
    order_items = user_order.orderitem_set.all()
    return render(request, "shop/order_success.html", {"order_items": order_items, "user_order": user_order})


@login_required(login_url="/login/")
def order_history(request):
    user_orders = Order.objects.filter(user=request.user).order_by('-created_at')
    orders_with_items = []

    for order in user_orders:
        order_items = order.orderitem_set.all()
        orders_with_items.append({
            'order': order,
            'order_items': order_items
        })

    return render(request, "shop/order_history.html",
                  {"orders_with_items": orders_with_items, "user_orders": user_orders})


@login_required(login_url="/login/")
def filtered_item(request, tag_names):
    tag_name_list = tag_names.split(',')
    items = Item.objects.all()
    for tag_name in tag_name_list:
        tag = Tags.objects.get(name=tag_name)
        items = items.filter(tags=tag)

    return render(request, "shop/filtered_item.html", {"items": items})
