from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile, Country, Location
from .forms import ProfileRegistrationForm


def edit_user(request):
    countries = Country.objects.all()
    locations = Location.objects.all()
    user_id = 2
    p = Profile()
    user = Profile.objects.get(user=user_id)
    context = {
        'user': user,
        'countries': countries,
        'locations': locations
    }
    return render(request, 'user/edit.html', context)

def profile_user(request):
    user_id = 2
    user = Profile.objects.get(user_id=user_id)
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
