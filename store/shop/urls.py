from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('men/', views.men_page, name="men"),
    path('woman/', views.woman_page, name="woman"),
]
