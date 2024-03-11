from django.core.management.base import BaseCommand
from homework_1.models import Product


class Command(BaseCommand):
    help = "create_product product."

    def handle(self, *args, **kwargs):
        for i in range(10):
            product = Product(product_name=f'IPhon{i}', cost=1000+i, quantity_product=i)
            product.save()
            self.stdout.write(f'{product}')
