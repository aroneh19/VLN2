from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Company
from .forms import CustomCompanyCreationForm, EditProfile
from job.models import Job

def register_view(request):
    """Renders the registration page and handles company registration.

    Returns:
    - Rendered HTTP response for company registration.
    """
    if request.method == 'POST':
        form = CustomCompanyCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            company = Company.objects.create(user=user)
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('login')
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')
            print(form.errors)
    else:
        form = CustomCompanyCreationForm()
    
    return render(request, 'user/register.html', {'form': form})

def companies_view(request):
    """Renders the page displaying all registered companies.

    Returns:
    - Rendered HTTP response displaying all companies.
    """
    companies = Company.objects.all()
    context = {
        'companies': companies
    }
    return render(request, 'company/companies.html', context)

def company_view(request):
    """Renders the page displaying details about a specific company and its jobs.

    Returns:
    - Rendered HTTP response displaying company details and its jobs.
    """ 
    company_id = request.GET.get('company_id')
    company = Company.objects.get(user=company_id)
    jobs = Job.objects.filter(company=company)
    context = {
        'company': company,
        'jobs': jobs
    }
    return render(request, 'company/company-info.html', context)

@login_required
def profile_view(request):
    """Renders the company's profile page.

    Returns:
    - Rendered HTTP response for the company's profile.
    """
    context = {
        'company': Company.objects.get(user=request.user)
    }
    return render(request, 'company/profile.html', context)

@login_required
def edit_view(request):
    """Renders the edit profile page and handles company profile editing.
    
    Returns:
    - Rendered HTTP response for editing company profile.
    """
    user = request.user
    company = Company.objects.get(user=user)

    if request.method == 'POST':
        form = EditProfile(request.POST, instance=company)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('company_profile')
        else:
            messages.error(request, 'Please correct the errors below.')
            messages.error(request, form.errors)
    else:
        form = EditProfile(instance=company)
    return render(request, "company/edit.html", {'form': form})
