from django.shortcuts import render, redirect
from .models import Application
from .forms import ApplicationForm
from user.models import Recommendation, Experience, Profile
from django.contrib.auth.decorators import login_required

@login_required
def application_form(request):
    job = request.GET.get('job_jid')
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
    user_profile = Profile.objects.get(user=request.user.id)
    recommendations = Recommendation.objects.filter(profile=user_profile)
    experiences = Experience.objects.filter(profile=user_profile)

    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.save()
            return redirect('application/confirmation_page')
    else:
        cover_letter = request.POST.get('cover_letter_hidden')

        context = {
            'user_profile': user_profile,
            'experiences': experiences,
            'recommendations': recommendations,
            'cover_letter': cover_letter,
            'form': ApplicationForm()
        }
        return render(request, 'application/review.html', context)

@login_required
def confirmation_page(request):
    return render(request, 'application/confirmation.html')

@login_required
def user_application(request):
    user_profile = Profile.objects.get(user = request.user.id)
    applications = Application.objects.filter(user=user_profile.user)
    return render(request, 'application/user_applications.html', {'applications': applications})
