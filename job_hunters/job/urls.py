from django.urls import path
from . import views

urlpatterns = [
    path('jobs/', views.job, name='jobs'),
    path('job/jobs/', views.filter_job_offerings, name='filter_job_offerings'),
    path('job_info/',views.job_info, name="job_info" ),
    path('post-job/', views.postjob_view, name='post_job'),
]