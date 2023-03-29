from django.shortcuts import render


def send_message(request):
    return render(request, "user_communication/index.html")

