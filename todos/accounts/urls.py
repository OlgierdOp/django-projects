from django.urls import path

from accounts.views import user_profile_view, register_request

urlpatterns = [
    path("", user_profile_view, name = 'home'),
    path("register/", register_request, name="register")
]
