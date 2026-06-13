from django.db import migrations
from django.contrib.auth import get_user_model


def create_default_users(apps, schema_editor):

    User = get_user_model()

    # ERP Super Admin (NOT Django superuser)
    if not User.objects.filter(username="admin").exists():
        User.objects.create_user(
            username="admin",
            email="admin@naiberi.com",
            password="Admin@12345",
            role="super_admin",
            is_staff=True,   # allows admin panel access
            is_superuser=False
        )

    # Optional viewer account
    if not User.objects.filter(username="viewer").exists():
        User.objects.create_user(
            username="viewer",
            email="viewer@naiberi.com",
            password="Viewer@12345",
            role="viewer",
            is_staff=False,
            is_superuser=False
        )


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_default_users),
    ]