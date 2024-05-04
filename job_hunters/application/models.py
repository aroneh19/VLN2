from django.db import models
from user.models import User
from job.models import Job

# Create your models here.
class Status(models.Model):
    sid = models.AutoField(primary_key=True)
    status = models.CharField(max_length=100)

class Application(models.Model):
    aid = models.AutoField(primary_key=True)
    date_applied = models.DateField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    cover_letter = models.TextField()
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    jid = models.ForeignKey(Job, on_delete=models.CASCADE)