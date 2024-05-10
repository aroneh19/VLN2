from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Profile, Country, Location
from .forms import CustomUserCreationForm, ProfileForm

def register_user(request):
    countries = Country.objects.all()
    locations = Location.objects.all()
    
    if request.method == 'POST':
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile.objects.create(user=user)
            return redirect('user_login')
        else:
            print(form.errors)
    else:
        form = CustomUserCreationForm()
    return render(request, 'user/register.html', {'form': form, 'countries': countries, 'locations': locations})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            print(form.errors)
            messages.error(request, 'Login failed!')
            messages.error(request, form.errors)
    context = {
        'form': AuthenticationForm()
    }
    return render(request, 'user/login.html', context)

@login_required
def profile_view(request):
    return render(request, "user/profile.html")


def edit_user(request):
    countries = Country.objects.all()
    locations = Location.objects.all()
    user_id = 2
    user = Profile.objects.get(user=user_id)
    context = {
        'user': user,
        'countries': countries,
        'locations': locations
    }
    return render(request, 'user/edit.html', context)

# def profile(request):
#     profile = Profile.objects.filter(user=request.user).first()
#     if request.method == 'POST':
#         form = ProfileForm(instance=profile, data=request.POST)
#         if form.is_valid():
#             profile = form.save(commit=False)
#             profile.user = request.user
#             profile.save()
#             return redirect('profile')
#     return render(request, 'user/profile.html', {'user': ProfileForm})





@login_required
def profile_view(request):
    countries = Country.objects.all()
    locations = Location.objects.all()
    user_profile = Profile.objects.get(user=request.user)
    context = {
        'user': user_profile,
        'countries': countries,
        'locations': locations
    }
    return render(request, "user/profile.html", context)

@login_required
def edit_profile(request):
    return render(request, "user/edit.html")
