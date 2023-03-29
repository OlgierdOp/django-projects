from crispy_forms.layout import Submit, Layout
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .decorators import unauthenticated_user, allowed_users
from .forms import PostForm, CreateUserForm, MessageForm
from .models import Post
from django.http import HttpResponse



@unauthenticated_user
def login_page(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('posts')
    else:
        form = AuthenticationForm()
    return render(request, 'posts/login.html', {'form': form})


@unauthenticated_user
def register_page(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request)
        if form.is_valid():
            form.save()
            return redirect('posts')

    return render(request, 'posts/user_register.html', {'form': form})


@login_required(login_url='login')
def post(request):
    posts = Post.objects.all()
    form = PostForm()
    form.helper.layout = Layout(
        'title',
        'content',
        Submit('submit', 'Publish', css_class='btn-success')
    )
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            user_post = form.save(commit=False)
            user_post.user = request.user
            user_post.save()
        return redirect('posts')
    return render(request, 'posts/home_posts.html', {'form': form, 'posts': posts})


@login_required(login_url='login')
def edit_post(request, pk):
    post1 = Post.objects.get(id=pk)

    form = PostForm(instance=post1)
    if post1.user == request.user:
        form.helper.add_input(Submit('submit', "Edit"))
        if request.method == "POST":
            form = PostForm(request.POST, instance=post1)
            if form.is_valid():
                form.save()
                return redirect('posts')
        return render(request, 'posts/post_edit.html', {'form': form})
    else:
        return redirect('posts')


@login_required(login_url='login')
def delete_post(request, pk):
    item = Post.objects.get(id=pk)

    if item.user == request.user:
        if request.method == "POST":
            item.delete()
            return redirect('posts')

        return render(request, 'posts/delete_post.html')
    else:
        return redirect('posts')


@login_required(login_url='login')
def send_message(request):
    form = MessageForm()
    if request.method == "POST":
        form = MessageForm(request.POST)
    return render(request, 'posts/send_message.html', {'form': form})


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def admin_page(request):
    return HttpResponse("Hello you are permitted to view this page")


def you_dont_have_access(request):
    return HttpResponse("YOU don't have access to this page please return to home page")
