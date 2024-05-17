from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from .models import Profile, Country, Location, Experience, Recommendation
from .forms import (CustomAuthenticationForm, CustomUserCreationForm, ProfileForm, 
                    UserChangeForm, RecommendationForm, ExperienceForm)

def register_view(request):
    """Renders the registration page and handles user registration.

    Returns:
    - Rendered HTTP response for registration.
    """    
    if request.method == 'POST':
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile.objects.create(user=user)
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('login')
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')
            messages.error(request, form.errors)
    context = {
        'form': CustomUserCreationForm(),
    }
    return render(request, 'user/register.html', context)

def login_view(request):
    """Renders the login page and handles user login.

    Returns:
    - Rendered HTTP response for login.
    """
    if request.method == "POST":
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('home')
        else:
            messages.error(request, 'Login failed!')
    context = {
        'form': CustomAuthenticationForm()
    }
    return render(request, 'user/login.html', context)

@login_required
def profile_view(request):
    """
    Renders the user's profile page with recommendations and experiences.

    Returns:
    - Rendered HTTP response for the user's profile.
    """
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
    """Renders the edit profile page and handles profile editing.

    Returns:
    - Rendered HTTP response for editing profile.
    """
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
            messages.success(request, 'Profile updated successfully.')
            return redirect('user_profile')
        else:
            messages.error(request, 'Please correct the errors below.')
            messages.error(request, user_form.errors)
            messages.error(request, profile_form.errors)

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
    """Renders the change password page and handles password change.

    Returns:
    - Rendered HTTP response for changing password.
    """
    user = request.user
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password changed successfully.')
            return redirect('home')
        else:
            messages.error(request, 'Password change failed!')
            messages.error(request, form.errors)
    else:
        form = PasswordChangeForm(user=user)
    context = {
        'form': form,
    }
    return render(request, 'user/change-password.html', context)

def add_recommendation(request):
    """Renders the recommendation form and handles adding a recommendation.

    Returns:
    - Rendered HTTP response for adding a recommendation.
    """
    if request.method == 'POST':
        form = RecommendationForm(request.POST)
        if form.is_valid():
            recommendation = form.save(commit=False)
            recommendation.profile = request.user.profile
            may_be_contacted = request.POST.get('checkbox', False)
            recommendation.may_be_contacted = may_be_contacted == "True"
            recommendation.save()
            return redirect('user_profile')
        else:
            messages.error(request, 'Failed to add recommendation. Please correct the errors below.')
            messages.error(request, form.errors)
    return render(request,'user/recommendation.html')
        
def add_experience(request):
    """Renders the experience form and handles adding an experience.

    Returns:
    - Rendered HTTP response for adding an experience.
    """
    if request.method == 'POST':
        form = ExperienceForm(request.POST)
        if form.is_valid():
            experience = form.save(commit=False)
            experience.profile = request.user.profile
            experience.save()
            return redirect('user_profile')
        else:
            messages.error(request, 'Failed to add experience. Please correct the errors below.')
            messages.error(request, form.errors)
    return render(request,'user/experience.html')
    
def delete_experience(request, eid):
    """Deletes the specified experience and redirects to the user's profile.

    Args:
    - eid: ID of the experience to delete.

    Returns:
    - Redirects to the user's profile after deleting the experience.
    """
    experience = Experience.objects.get(eid = eid)
    experience.delete()
    return redirect('user_profile') 

def delete_recommendation(request, rid):
    """Deletes the specified recommendation and redirects to the user's profile.

    Args:
    - rid: ID of the recommendation to delete.

    Returns:
    - Redirects to the user's profile after deleting the recommendation.
    """
    recommendation = Recommendation.objects.get(rid = rid)
    recommendation.delete()
    return redirect('user_profile')
 
def c_or_u_login(request):
    """Renders the choice between company or user login page.

    Returns:
    - Rendered HTTP response for choosing between company or user login.
    """
    return render(request, 'user/comp_or_login.html')

def c_or_u_signup(request):
    """Renders the choice between company or user signup page.

    Returns:
    - Rendered HTTP response for choosing between company or user signup.
    """
    return render(request, 'user/comp_or_user_signup.html')