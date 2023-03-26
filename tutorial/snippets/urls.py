from django.urls import path, include
from rest_framework.routers import DefaultRouter

from snippets import views
from cars.urls import car_router

# from tutorial.urls import router

router = DefaultRouter()
router.register(r"snippets", views.SnippetViewSet, basename="snippet")
router.register(r"users", views.UserViewSet, basename="user")

router.registry.extend(car_router.registry)

urlpatterns = [path("", include(router.urls))]
