from django.core.management.base import BaseCommand
from apprac.models import User, Profile
from faker import Faker
import random

fake = Faker()
class Command(BaseCommand):
    help = 'Generates fake Users and Profile'
    def handle(self, *args, **option):
        for _ in range(10):
            u = User.objects.create(
                name = fake.name(),
                active = True
            )
            Profile.objects.create(
                user = u,
                role = u,
                phone_no = '+',
            )    
        self.stdout.write(self.style.SUCCESS('Fake User Profile generated.'))
 