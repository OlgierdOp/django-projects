from django.contrib import admin
from django.urls import path
from main import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home),
    path('admin_panel', views.admin, name='admin_panel'),
    path('login_page', views.login_page, name='login_page'),
    path('logout', LogoutView.as_view(next_page="/"), name="logout"),
    path('order/<str:id>', views.order, name="order"),
    path('register', views.register_view, name="register"),
    path('constructor_panel', views.constructor_panel_view, name="constructor_panel"),
    path('client_messanger_view', views.client_orders_panel, name="client_messanger_view")
]
