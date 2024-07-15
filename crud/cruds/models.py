from django.db import models


class detail(models.Model):
    name = models.CharField(max_length=60)
    branch = models.CharField(max_length=50)
    section = models.CharField(max_length=5)
    year = models.IntegerField()
    dob = models.DateField()
    email_id = models.EmailField(max_length=80, unique=True)
    password = models.CharField(max_length=20)


