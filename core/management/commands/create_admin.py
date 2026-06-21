from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth import get_user_model
import os

@receiver(post_migrate)
def create_superuser_on_migrate(sender, **kwargs):
    # This runs automatically after your database migrations finish
    User = get_user_model()
    username = os.getenv('DJANGO_SUPERUSER_USERNAME', 'admin')
    email = os.getenv('DJANGO_SUPERUSER_EMAIL', 'admin@naiberi.com')
    password = os.getenv('DJANGO_SUPERUSER_PASSWORD', 'naiberi@123')

    user, created = User.objects.get_or_create(username=username)
    user.email = email
    user.set_password(password)
    user.is_staff = True
    user.is_superuser = True
    user.is_active = True
    # If you have a custom role field, uncomment the line below:
    # user.role = 'Super Admin' 
    user.save()
    print(f"DEBUG: Superuser {username} enforced by migration signal.")