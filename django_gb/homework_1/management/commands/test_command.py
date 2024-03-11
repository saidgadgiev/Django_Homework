from django.core.management.base import BaseCommand
from homework_1.models import Client


class Command(BaseCommand):
    help = "Get all users."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        client = Client.objects.filter(pk=pk)
        self.stdout.write(f'{client}')
