from django.db import models

# Create your models here.
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    ssn = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='company_logo/')
    cover = models.ImageField(upload_to='company_cover/')
    description = models.TextField()
    website = models.URLField()