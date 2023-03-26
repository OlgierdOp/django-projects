from django.urls import path

from .views import tasks_list, task_details

urlpatterns = [
    path("", tasks_list),
    path("<int:id>/", task_details),
]