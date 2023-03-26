from django.urls import path
from .views import calculator, home, operation

urlpatterns = [
    path("", home),
    path("<op>/", operation),
    path("<op>/<int:a>/<int:b>/", calculator)
]
