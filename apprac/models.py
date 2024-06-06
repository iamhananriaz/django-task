from django.db import models
from django.core.exceptions import ValidationError
from django.db.models import fields
from django.utils import timezone
from django.contrib.auth.models import User 



class User(models.Model):
    name = models.CharField(max_length=50)
    active = models.BooleanField()
class Profile(models.Model):
    user = models.CharField(max_length=10)
    phone_no = models.CharField(max_length = 13)
    role = models.CharField(max_length=10)

