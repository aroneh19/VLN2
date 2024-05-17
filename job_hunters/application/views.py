from django.shortcuts import render, redirect
from .models import Application
from .forms import ApplicationForm
from user.models import Recommendation, Experience, Country, Profile
from django.contrib.auth.decorators import login_required

@login_required
def application_form(request):
    job = request.GET.get('job_jid')
    user_profile = Profile.objects.get(user=request.user.id)  # Retrieve the Profile object for the logged-in user
    recommendations = Recommendation.objects.filter(profile=user_profile)
    experiences = Experience.objects.filter(profile=user_profile)
    countries = Country.objects.all()
    context = {
        'recommendations': recommendations,
        'experiences': experiences,
        'countries': countries,
        'user_profile': user_profile,
        'job': job
    }
    return render(request, 'application/application.html', context)

@login_required
def submit_application(request):
    print(request.POST)
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.save()
        else:
            print(form.errors)
        return redirect('jobs')
    return redirect('jobs')

@login_required
def user_application(request):
    user_profile = Profile.objects.get(user = request.user.id)
    applications = Application.objects.filter(user=user_profile.user)
    return render(request, 'application/user_applications.html', {'applications': applications})
