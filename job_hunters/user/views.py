from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from .models import Profile, Country, Location, Experience, Recommendation
from .forms import CustomUserCreationForm, ProfileForm, UserChangeForm, RecommendationForm, ExperienceForm

def register_view(request):    
    if request.method == 'POST':
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile.objects.create(user=user)
            return redirect('user_login')
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')
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
            messages.error(request, 'Login failed!')
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
    user = request.user
    profile = Profile.objects.get(user=user)
    countries = Country.objects.all()
    locations = Location.objects.all()

    if request.method == 'POST':
        user_form = UserChangeForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('user_profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        user_form = UserChangeForm(instance=user)
        profile_form = ProfileForm(instance=profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'countries': countries,
        'locations': locations,
    }
    return render(request, 'user/edit.html', context)

@login_required
def change_password(request):
    user = request.user
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=user)
        if form.is_valid():
            form.save()
            messages.info(request, 'Your password was successfully updated!')
            return redirect('user_profile')
        else:
            messages.error(request, 'Password change failed!')
    else:
        form = PasswordChangeForm(user=user)
    context = {
        'form': form,
    }
    return render(request, 'user/change-password.html', context)

def add_recommendation(request):
    if request.method == 'POST':
        form = RecommendationForm(request.POST)
        if form.is_valid():
            recommendation = form.save(commit=False)
            recommendation.profile = request.user.profile
            recommendation.save()
            messages.success(request, 'Recommendation added successfully!')
            return redirect('user_profile')
        else:
            messages.error(request, 'Failed to add recommendation. Please correct the errors below.')
    return render(request,'user/recommendation.html')
        
def add_experience(request):
    if request.method == 'POST':
        form = ExperienceForm(request.POST)
        if form.is_valid():
            experience = form.save(commit=False)
            experience.profile = request.user.profile
            experience.save()
            messages.success(request, 'Experience added successfully!')
            return redirect('user_profile')
        else:
            messages.error(request, 'Failed to add experience. Please correct the errors below.')
    return render(request,'user/experience.html')
    
def delete_experience(request, eid):
    experience = Experience.objects.get(eid = eid)
    experience.delete()
    return redirect('user_profile') 

def delete_recommendation(request, rid):
    recommendation = Recommendation.objects.get(rid = rid)
    recommendation.delete()
    return redirect('user_profile')
 