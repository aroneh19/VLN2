from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Profile, Country, Location, Experience, Recommendation
from .forms import CustomUserCreationForm, ProfileForm

def register_view(request):    
    if request.method == 'POST':
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile.objects.create(user=user)
            return redirect('user_login')
        else:
            print(form.errors)
    context = {
        'form': CustomUserCreationForm(),
    }
    
    return render(request, 'user/register.html', context)


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            profile_exists = Profile.objects.filter(user=user).exists()
            if profile_exists:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Profile does not exist!')
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
    profile = Profile.objects.get(user=request.user)
    recommendation = Recommendation.objects.filter(profile=profile)
    experience = Experience.objects.filter(profile=profile)
    context = {
        'profile': profile,
        'recommendations': recommendation,
        'experiences': experience
    }
    return render(request, "user/profile.html", context)

@login_required
def edit_view(request):
    profile = Profile.objects.get(user=request.user)
    countries = Country.objects.all()
    locations = Location.objects.all()

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('user_profile')
        else:
            print(form.errors)
    else:
        form = ProfileForm(instance=profile)

    context = {
        'profile': profile,
        'countries': countries,
        'locations': locations,
        'form': form,
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
