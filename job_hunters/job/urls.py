from django.urls import path
from . import views

urlpatterns = [
    path('jobs.html/', views.job, name='jobs'),
    path('job/jobs.html/', views.filter_job_offerings, name='filter_job_offerings'),
    path('job_info.html/',views.job_info, name="job_info" ),
    path('post-job/', views.postjob_view, name='post_job'),
]