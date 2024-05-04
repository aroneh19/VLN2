from django.db import models

# Create your models here.
from django.db import models


class Location(models.Model):
    postcode = models.IntegerField()
    city = models.CharField(max_length=100)

class Country(models.Model):
    country = models.CharField(max_length=100)

class User(models.Model):
    ssn = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    street_name = models.CharField(max_length=255)
    house_number = models.CharField(max_length=10)
    picture = models.ImageField(upload_to='user_pictures/', blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)

class Experience(models.Model):
    place_of_work = models.CharField(max_length=255)
    role = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)


class Recommendation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    role = models.CharField(max_length=100)
    may_be_contacted = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)