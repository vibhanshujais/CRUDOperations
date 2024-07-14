from django.db import models


class crud(models.Model):
    name = models.CharField(max_length=60)
    branch = models.CharField(max_length=50)
    section = models.CharField(max_length=5)
    year = models.IntegerField()
    dob = models.DateField()
    
