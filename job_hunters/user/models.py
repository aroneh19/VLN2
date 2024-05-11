from django.db import models
from django.contrib.auth.models import User

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

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone = models.CharField(max_length=20)
    street_name = models.CharField(max_length=255)
    house_number = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    picture = models.URLField()
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.user.username


class Experience(models.Model):
    eid = models.AutoField(primary_key=True)
    place_of_work = models.CharField(max_length=255)
    role = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.place_of_work} - {self.role}"


class Recommendation(models.Model):
    rid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    role = models.CharField(max_length=100)
    may_be_contacted = models.BooleanField(default=False)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name