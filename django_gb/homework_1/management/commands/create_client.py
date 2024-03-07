from django.core.management.base import BaseCommand
from homework_1.models import Client


class Command(BaseCommand):
    help = "create_client client."

    def handle(self, *args, **kwargs):
        for i in range(5):
            client = Client(name=f'Client{i}', email=f'email{i}@example.com', phone_number=f'{i}{i}{i}{i}{i}{i}{i}{i}', address=f'address{i}')
            client.save()
            self.stdout.write(f'{client}')
