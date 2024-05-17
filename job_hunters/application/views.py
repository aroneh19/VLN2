from django.shortcuts import render, redirect
from .models import Application
from job.models import Job
from .forms import ApplicationForm
from user.models import Recommendation, Experience, Profile
from django.contrib.auth.decorators import login_required

@login_required
def application_form(request):
    job_id = request.GET.get('job_jid')
    job = Job.objects.get(jid = job_id)
    user_profile = Profile.objects.get(user=request.user.id)
    recommendations = Recommendation.objects.filter(profile=user_profile)
    experiences = Experience.objects.filter(profile=user_profile)

    if request.method == 'POST':
        cover_letter = request.POST.get('cover_letter')
        request.session['cover_letter'] = cover_letter
        return redirect('review', job_jid=job_id)

    context = {
        'recommendations': recommendations,
        'experiences': experiences,
        'user_profile': user_profile,
        'job': job,
    }
    return render(request, 'application/application.html', context)


@login_required
def review(request):
    user_profile = Profile.objects.get(user=request.user.id)
    recommendations = Recommendation.objects.filter(profile=user_profile)
    experiences = Experience.objects.filter(profile=user_profile)

    cover_letter = request.GET.get('cover_letter', '')
    job_id = request.GET.get('job_jid')
    job = Job.objects.get(jid = job_id)
    context = {
        'user_profile': user_profile,
        'experiences': experiences,
        'recommendations': recommendations,
        'cover_letter': cover_letter,
        'job': job,
        'form': ApplicationForm()
    }
    return render(request, 'application/review.html', context)

def submit_review(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.save()
            return redirect('application/confirmation_page')
    else:
        redirect('jobs')

@login_required
def confirmation_page(request):
    return render(request, 'application/confirmation.html')

@login_required
def user_application(request):
    user_profile = Profile.objects.get(user = request.user.id)
    applications = Application.objects.filter(user=user_profile.user)
    return render(request, 'application/user_applications.html', {'applications': applications})
