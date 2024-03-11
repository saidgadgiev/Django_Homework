from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = models.IntegerField(max_length=12)
    address = models.CharField(max_length=100)
    date_registration = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Имя клиента: {self.name}'


class Product(models.Model):
    product_name = models.CharField(max_length=30)
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    quantity_product = models.IntegerField()  # Количества продукта
    data_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name


class Oder(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    order_summ = models.DecimalField(max_digits=6, decimal_places=2)
    date_order = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Номер заказа {self.id}, от {self.date_order} клиент: {self.client.name}'
