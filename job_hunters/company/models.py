from django.db import models

# Create your models here.
class Company(models.Model):
    cid = models.AutoField(primary_key=True)
    ssn = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=100)
    logo = models.URLField(default="http://t1.gstatic.com/licensed-image?q=tbn:ANd9GcR0NrOJEpfjkM0zxD-aO9b-bWqW3mhY57jPMg3aSbxTYO__R4jOvx8T2Oa7Fm9yxXOGg4B_ns3SZaZGCiBOPQw")
    cover = models.URLField(default="http://t1.gstatic.com/licensed-image?q=tbn:ANd9GcR0NrOJEpfjkM0zxD-aO9b-bWqW3mhY57jPMg3aSbxTYO__R4jOvx8T2Oa7Fm9yxXOGg4B_ns3SZaZGCiBOPQw")
    description = models.TextField()
    website = models.URLField()

    def __str__(self):
        return self.name