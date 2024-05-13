from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Company
from .forms import CustomCompanyCreationForm

def register_view(request):
    if request.method == 'POST':
        form = CustomCompanyCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            company = Company.objects.create(user=user)
            return redirect('company_login')
        else:
            print(form.errors)
    else:
        form = CustomCompanyCreationForm()
    
    return render(request, 'user/register.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            profile_exists = Company.objects.filter(user=user).exists()
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
    return render(request, 'company/login.html', context)


@login_required
def profile_view(request):
    context = {
        'company': Company.objects.get(user=request.user)
    }
    return render(request, 'company/profile.html', context)


@login_required
def edit_view(request):
    return render(request, "company/edit.html")

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
            messages.error(request, form.errors)
    else:
        form = PasswordChangeForm(user=user)
    context = {
        'form': form,
    }
    return render(request, 'user/change-password.html', context)
