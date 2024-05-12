from django.shortcuts import render, redirect
from django.contrib import messages
from user.models import Profile
from company.models import Company
from job.models import Job
from random import sample, seed
from datetime import date


def random_daily_jobs(num_jobs = 8):
    jobs = list(Job.objects.filter(start_date__lte=date.today(), end_date__gte=date.today()))
    seed(str(date.today))
    sampled_jobs = sample(jobs, num_jobs)
    return sampled_jobs


def home(request):
    jobs = random_daily_jobs()
    context = {
        'jobs': jobs,
    }
    if request.user.is_authenticated:
        is_company = Company.objects.filter(user=request.user).exists()
        if is_company:
            photo = Company.objects.get(user=request.user).logo
        else:
            photo = Profile.objects.get(user=request.user).picture
        context.update({
            'is_company': is_company,
            'photo': photo,
        })
    return render(request, 'index.html', context)


def handler404(request, *args, **argv):
    messages.error(request, 'The page you were looking does not exist.')
    return redirect('home')

def handler500(request, *args, **argv):
    messages.error(request, "Something bad happened, we are very sorry.")
    return redirect('home')