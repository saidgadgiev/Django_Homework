from django.core.management.base import BaseCommand
from homework_1.models import Client


class Command(BaseCommand):
    help = "Get all users."

    def handle(self, *args, **kwargs):
        client = Client.objects.all()
        for i in client:
            self.stdout.write(f'{i}')
