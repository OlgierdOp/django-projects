from django.urls import path

from posts.views import post_list, post_details

app_name = "posts"
urlpatterns = [
    path("", post_list, name="list"),
    path("<int:id>/", post_details, name="details"),
]