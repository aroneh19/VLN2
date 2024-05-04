from django.db import models
from user.models import User
from joboffer.models import JobOffer

# Create your models here.
class Status(models.Model):
    status = models.CharField(max_length=100)

class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(JobOffer, on_delete=models.CASCADE)
    date_applied = models.DateField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    cover_letter = models.TextField()