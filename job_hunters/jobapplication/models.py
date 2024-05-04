from django.db import models
from user.models import User
from joboffer.models import JobOffer

# Create your models here.
class JobApplication(models.Model):
    app_id = models.AutoField(primary_key=True)
    job_id = models.ForeignKey(JobOffer, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date_applied = models.DateField()
    status = models.CharField(max_length=100)
    cover_letter = models.TextField()