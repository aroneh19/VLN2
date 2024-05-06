from django.shortcuts import render
from .models import Company

def register(request):
    return render(request, 'company/register.html')

def login(request):
    return render(request, 'company/login.html')