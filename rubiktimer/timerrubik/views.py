from django.shortcuts import render, redirect
from forms import NumberField
def calculate(request):
    if request.method == 'POST':
        form = NumberField()
        if form.is_valid():
            number_1 = form.cleaned_data['number_1']