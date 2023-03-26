from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserProfileForm , NewUserForm
from django.contrib.auth import authenticate, login
from django.contrib import messages


def user_profile_view(request):
    if not request.user.is_authenticated:
        return HttpResponse("Nie możesz tu byc")

    if request.method == "POST":
        form = UserProfileForm(instance=request.user.userprofile, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()

    form = UserProfileForm(instance=request.user.userprofile)
    return render(
        request,
        "accounts/profile.html",
        {"form": form}

    )


def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        ...
    else:
        ...


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("home")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="registration/register.html", context={"register_form": form})

