from django.db import models
from company.models import Company

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

class JobType(models.Model):
    type = models.CharField(max_length=100)

class Job(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    job_type = models.ForeignKey(JobType, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    start_date = models.DateField()
    due_date = models.DateField()
    description = models.TextField()