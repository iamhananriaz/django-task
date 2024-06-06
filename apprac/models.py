from django.db import models
from django.core.exceptions import ValidationError
from django.db.models import fields
from django.utils import timezone
from django.contrib.auth.models import User 



class User(models.Model):
    name = models.CharField(max_length=50)
    active = models.BooleanField()

class PhoneField(models.Field):
                   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def get_prep_value(self, value):
        return str(value)
    
    def db_type(self, connection):
        return f"char({13})"
        
fields.PhoneField = PhoneField 

class Profile(models.Model):
    user = models.CharField(max_length=10)
    phone_no = PhoneField(max_length = 13)
    role = models.CharField(max_length=10)

