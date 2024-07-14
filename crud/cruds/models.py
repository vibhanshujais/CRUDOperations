from django.db import models


class crud(models.Model):
    name = models.CharField(max_length=60)
    dob = models.DateField()
    year = models.IntegerField()
    branch = models.CharField(max_length=50)
    
