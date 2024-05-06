from django.db import models

# Create your models here.
from django.db import models

from datetime import datetime


class Location(models.Model):
    lid = models.AutoField(primary_key=True)
    postcode = models.IntegerField()
    city = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.postcode}"

class Country(models.Model):
    coid = models.AutoField(primary_key=True)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.country

class User(models.Model):
    uid = models.AutoField(primary_key=True)
    ssn = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    street_name = models.CharField(max_length=255)
    house_number = models.CharField(max_length=10)
    date_of_birth = models.DateField(default=datetime(2000, 1, 1).date())
    picture = models.URLField()
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)

class Experience(models.Model):
    eid = models.AutoField(primary_key=True)
    place_of_work = models.CharField(max_length=255)
    role = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Recommendation(models.Model):
    rid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    role = models.CharField(max_length=100)
    may_be_contacted = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)