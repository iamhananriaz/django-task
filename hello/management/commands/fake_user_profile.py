from django.core.management.base import BaseCommand
from hello.models import User, Profile
from faker import Faker
from django.http import HttpResponse
import random

fake = Faker()
class Command(BaseCommand):

    def handle(self):
        self.stdout.write(self.style.SUCCESS('Fake User Profile generated.'))
        
