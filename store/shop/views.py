from django.shortcuts import render
from .forms import ItemForm
from .models import Item


# Create your views here.
def home(request):
    form = ItemForm()
    return render(request, 'shop/home.html', {'form': form})


def men_page(request):
    items = Item.objects.filter(gender="M")
    return render(request, 'shop/men_products.html', {'items': items})


def woman_page(request):
    items = Item.objects.filter(gender="F")
    return render(request, 'shop/woman_products.html', {'items': items})
