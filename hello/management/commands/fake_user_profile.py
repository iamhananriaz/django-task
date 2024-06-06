from django.core.management.base import BaseCommand
from hello.models import User, Profile
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
                email = u,
                phone_no = '+' + str(9230 + random.randint(0, 4)) + str(random.randint(10000000, 100000000 )),
            )    
        self.stdout.write(self.style.SUCCESS('Fake User Profile generated.'))
 