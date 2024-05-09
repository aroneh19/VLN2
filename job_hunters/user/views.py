from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import User, Country, Location
from .forms import ProfileRegistrationForm


def edit_user(request):
    user_id = 3
    user = User.objects.get(uid=user_id)
    return render(request, 'user/edit.html', {'user': user})

def profile_user(request):
    user_id = 3
    user = User.objects.get(uid=user_id)
    return render(request, 'user/profile.html', {'user': user})

def register_user(request):
    countries = Country.objects.all()
    locations = Location.objects.all()
    
    if request.method == 'POST':
        form = ProfileRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_login')
    else:
        form = ProfileRegistrationForm()
    
    return render(request, 'user/register.html', {'form': form, 'countries': countries, 'locations': locations})
