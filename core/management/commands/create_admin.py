import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Creates an admin user with Super Admin role'

    def handle(self, *args, **options):
        User = get_user_model()
        username = os.getenv('DJANGO_SUPERUSER_USERNAME', 'admin')
        email = os.getenv('DJANGO_SUPERUSER_EMAIL', 'admin@naiberi.com')
        password = os.getenv('DJANGO_SUPERUSER_PASSWORD', 'naiberi@123')

        if not User.objects.filter(username=username).exists():
            # Create the superuser and explicitly set the role to 'super_admin'
            user = User.objects.create_superuser(
                username=username, 
                email=email, 
                password=password
            )
            user.role = 'Super Admin'  # Mapping to your User model's choices
            user.save()
            self.stdout.write(self.style.SUCCESS(f'Superuser {username} created with role: Super Admin'))
        else:
            self.stdout.write(self.style.WARNING(f'Superuser {username} already exists.'))