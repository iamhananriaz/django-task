from django.core.management.base import BaseCommand
from apprac.models import User, Profile

class Command(BaseCommand):
    help = "Populate Data"

    def handle(self, *args, **kwargs):
        for x in range(10):
            u = User.objects.create(
                name = x,
                active = True
            )
            Profile.objects.create(
                user = u,
                role = u,
                phone_no = '+',
            )    
        u = Profile.objects.all().count()
        self.stdout.write(self.style.SUCCESS('Fake User Profile generated.'))
 