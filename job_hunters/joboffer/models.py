from django.db import models
from company.models import Company

# Create your models here.
class JobOffer(models.Model):
    job_id = models.AutoField(primary_key=True)
    comapny_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    job_type = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    start_date = models.DateField()
    due_date = models.DateField()
    description = models.TextField()