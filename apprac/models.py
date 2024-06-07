from django.db import models
from django.contrib.auth.models import User 


class Profile(models.Model):
    user = models.CharField(max_length=10)
    phone_no = models.CharField(max_length = 13)
    role = models.CharField(max_length=10)

class User(models.Model):
    name = models.CharField(max_length=10)
    active = models.BooleanField(default=True)

class info(models.Model):
    name = models.CharField(max_length=32)
    about = models.TextField(blank=True, default="")

    def __str__(self):
        return self.about or self.name