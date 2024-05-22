from random import choices
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    GENDER_CHOICES = [
        ("M", "Male"),
        ("F", "Female"),
    ]
    name = models.CharField(max_length=30)
    nickname = models.CharField(max_length=30, unique=True)
    email = models.EmailField()
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1)
    date_of_birth = models.DateField()
    subscription = models.BooleanField()

