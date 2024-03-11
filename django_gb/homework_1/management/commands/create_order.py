from django.core.management.base import BaseCommand
from homework_1.models import Client, Oder, Product


class Command(BaseCommand):
    help = "Create order"

    def add_arguments(self, parser):
        parser.add_argument("id_client", type=int, help="client ID")
        parser.add_argument('-p', '--id_product', nargs='+', help="client ID", required=True)

    def handle(self, *args, **kwargs):
        id_client = kwargs.get('id_client')
        id_product: list = kwargs.get('id_product')

        client = Client.objects.filter(pk=id_client).first()

        order = Oder(client=client)
        total_price = 0
        for i in range(0, len(id_product)):
            producti = Product.objects.filter(pk=id_product[i]).first()
            total_price += float(producti.cost)
            order.order_summ = total_price
            order.save()
            order.product.add(producti)
