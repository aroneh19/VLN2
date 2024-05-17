from django.shortcuts import render
from job.models import Job
from random import sample, seed
from datetime import date


def random_daily_jobs(num_jobs = 16):
    date_today = date.today()
    jobs = list(Job.objects.filter(date_of_offering__lte=date_today, due_date__gte=date_today))

    if len(jobs) < num_jobs:
        num_jobs = len(jobs)

    seed(str(date.today))
    sampled_jobs = sample(jobs, num_jobs)
    return sampled_jobs

def home(request):
    jobs = random_daily_jobs()
    context = {
        'jobs': jobs,
    }
    return render(request, 'index.html', context)

def zavant(request):
    return render(request, 'why_zavant.html')
