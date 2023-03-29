from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('men/', views.men_page, name="men"),
    path('woman/', views.woman_page, name="woman"),
    path('', views.main_page, name="main"),
    path('login/', views.login_page, name="login_page"),
    path('register/', views.register_page, name="register_page"),
]
