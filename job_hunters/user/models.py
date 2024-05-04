from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    ssn = models.IntegerField(unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='user_pictures/', blank=True, null=True)