from django.contrib import admin
from django.urls import path
from main import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home),
    path('admin_panel', views.admin),
    path('login_page', views.login_page, name='login_page'),
    path('logout', LogoutView.as_view(next_page="/"), name="logout"),
    path('order/<str:id>', views.order, name="order")
]
