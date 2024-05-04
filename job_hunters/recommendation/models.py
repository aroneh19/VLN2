from django.db import models
from user.models import User

# Create your models here.
class Recommendation(models.Model):
    recom_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    role = models.CharField(max_length=100)
    may_contact = models.BooleanField(default=False)