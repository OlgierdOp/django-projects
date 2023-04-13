from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('men/', views.men_page, name="men"),
    path('woman/', views.woman_page, name="woman"),
    path('', views.main_page, name="main"),
    path('login/', views.login_page, name="login_page"),
    path('register/', views.register_page, name="register_page"),
    path('logout/', LogoutView.as_view(next_page="home"), name="logout"),
    path('buy/<str:id>/', views.buy, name="buy"),
    path('cart/', views.cart, name="cart"),
    path('add_to_cart/<str:id>', views.add_to_cart, name="add_to_cart"),
    path('delete_item_from_cart/<int:id>/', views.delete_item_from_cart, name="delete_item_from_cart"),
    path('admin_panel/', views.admin_panel, name="admin_panel"),
]
