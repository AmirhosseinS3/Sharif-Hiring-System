from django.contrib.auth.models import User
from django.db import models


class Employee(User):
    name = models.CharField(max_length=30, null=False)
    confirmation_code = models.CharField(max_length=6)
    activated = models.BooleanField(default=False)


class Employer(User):
    name = models.CharField(max_length=30, null=False, primary_key=True)
    address = models.CharField(max_length=500, null=False)
    description = models.CharField(max_length=2000, null=False)
    confirmation_code = models.CharField(max_length=6)
    activated = models.BooleanField(default=False)
