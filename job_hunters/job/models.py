from django.db import models
from company.models import Company
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    caid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

class JobType(models.Model):
    joid = models.AutoField(primary_key=True)
    type = models.CharField(max_length=100)

class Job(models.Model):
    jid = models.AutoField(primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    jobtype = models.ForeignKey(JobType, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_of_offering = models.DateField()
    due_date = models.DateField()
    start_date = models.DateField()
    description = models.TextField()
    