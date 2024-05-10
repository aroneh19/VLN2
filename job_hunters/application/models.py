from django.db import models
from user.models import User
from job.models import Job
from django.utils import timezone

# Create your models here.
class Status(models.Model):
    sid = models.AutoField(primary_key=True)
    status = models.CharField(max_length=100)

class Application(models.Model):
    aid = models.AutoField(primary_key=True)
    date_applied = models.DateField(default=timezone.now())
    status = models.ForeignKey(Status, on_delete=models.CASCADE, default= 1)
    cover_letter = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)