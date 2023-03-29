from django.urls import path
from .views import send_message

app_name = "user_communication"

urlpatterns = [
    path('', send_message),
]
