from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import post, edit_post, delete_post, register_page, login_page, send_message, admin_page, \
    you_dont_have_access

urlpatterns = [
    path('posts/', post, name='posts'),
    path('edit_post/<str:pk>', edit_post, name='edit_post'),
    path('delete_post/<str:pk>', delete_post, name='delete_post'),
    path('register/', register_page, name='register'),
    path('login/', login_page, name="login"),
    path('logout/', LogoutView.as_view(next_page="posts"), name='logout'),
    path('message/', send_message, name='send_message'),
    path('admin_page', admin_page, name='admin_page'),
    path('no_access', you_dont_have_access, name='no_access')
]
