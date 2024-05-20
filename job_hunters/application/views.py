from django.shortcuts import render, redirect
from .models import Application
from job.models import Job
from user.models import User
from .forms import ApplicationForm
from user.models import Recommendation, Experience, Profile
from django.contrib.auth.decorators import login_required

@login_required
def application_form(request):
    """Renders the application form page for a specific job.

    Returns:
    - Rendered HTTP response for the application form page.
    """
    job_id = request.GET.get('job_jid')
    job = Job.objects.get(jid = job_id)
    user_profile = Profile.objects.get(user=request.user.id)
    recommendations = Recommendation.objects.filter(profile=user_profile)
    experiences = Experience.objects.filter(profile=user_profile)

    context = {
        'recommendations': recommendations,
        'experiences': experiences,
        'user_profile': user_profile,
        'job': job,
    }
    return render(request, 'application/application.html', context)

@login_required
def review(request):
    """Renders the review page for the application before submission.

    Returns:
    - Rendered HTTP response for the review page.
    """
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

@login_required
def submit_review(request):
    """Handles the submission of an application.

    Returns:
    - Rendered HTTP response for the confirmation page or redirects to the jobs page.
    """
    if request.method == 'POST':
        cover_letter = request.POST.get('cover_letter')
        user_id = request.user.id
        job_id = request.POST.get('job_jid')
        user = User.objects.get(id=user_id)
        job = Job.objects.get(jid=job_id)

        application = Application(
            user=user,
            job=job,
            cover_letter=cover_letter
        )
        application.save()
        return confirmation_page(request)
    else:
        return redirect('jobs')


@login_required
def confirmation_page(request):
    """
    Renders the confirmation page after submitting an application.

    Returns:
    - Rendered HTTP response for the confirmation page.
    """
    return render(request, 'application/confirmation.html')

@login_required
def user_application(request):
    """Renders the page displaying applications submitted by the current user.

    Returns:
    - Rendered HTTP response for the user's applications page.
    """
    user_profile = Profile.objects.get(user = request.user.id)
    applications = Application.objects.filter(user=user_profile.user)
    return render(request, 'application/user_applications.html', {'applications': applications})
