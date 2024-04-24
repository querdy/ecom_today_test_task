from django.contrib.auth import get_user_model
from django.core.management import BaseCommand

User = get_user_model()


class Command(BaseCommand):

    def handle(self, *args, **options):
        if not User.objects.filter(username="admin").exists():
            username = "admin"
            email = "admin@admin.ru"
            password = "admin"
            admin = User.objects.create_superuser(
                email=email, username=username, password=password
            )
            admin.save()
