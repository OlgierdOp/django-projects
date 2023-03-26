from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cars import views
# from snippets.urls import router
car_router = DefaultRouter()
car_router.register(r"cars", views.CarViewSet, basename="car")

# urlpatterns = [path("", include(router.urls))]
