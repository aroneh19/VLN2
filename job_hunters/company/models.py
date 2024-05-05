from django.db import models

# Create your models here.
class Company(models.Model):
    cid = models.AutoField(primary_key=True)
    ssn = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    logo = models.URLField()
    cover = models.URLField()
    description = models.TextField()
    website = models.URLField()