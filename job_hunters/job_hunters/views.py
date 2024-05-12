from django.shortcuts import render, redirect
from django.contrib import messages
from user.models import Profile
from company.models import Company
from django.contrib.auth.models import User


def jobs():
    # Sækja störf sem henta á home page
    pass


def home(request):
    if request.user.is_authenticated:
        is_company = Company.objects.filter(user=request.user).exists()
        if is_company:
            photo = Company.objects.get(user=request.user).logo
        else:
            photo = Profile.objects.get(username=request.user).picture
        context = {
            'is_company': is_company,
            'photo': photo,
        }
        return render(request, 'index.html', context)
    return render(request, 'index.html')


def handler404(request, *args, **argv):
    messages.error(request, 'The page you were looking does not exist.')
    return redirect('home')

def handler500(request, *args, **argv):
    messages.error(request, "Something bad happened, we are very sorry.")
    return redirect('home')