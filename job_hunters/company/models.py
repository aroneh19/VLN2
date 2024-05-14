from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    address = models.CharField(max_length=100)
    logo = models.URLField()
    cover = models.URLField()
    description = models.TextField()
    website = models.URLField()

    # def available_jobs(self):
    #     return self.jobs.filter(is_available=True).count()

    def __str__(self):
        return self.user.first_name