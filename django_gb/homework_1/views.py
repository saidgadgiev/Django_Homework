from datetime import datetime, timedelta

from django.http import HttpResponse
from django.shortcuts import render, redirect
import logging
from .models import Client, Product, Oder
from .forms import GetProductClientDays


logger = logging.getLogger(__name__)

menu = [
    {'title': 'Главная страница', 'url_name': 'home'},
    {'title': 'Интернет Магазин', 'url_name': 'online_store'},
    {'title': 'О сайте', 'url_name': 'about'},
    ]

connectionType = [
    {'title': 'Оптика', 'url_name': 'optika'},
    {'title': 'Медь', 'url_name': 'copper'},
    {'title': 'Радиоволна', 'url_name': 'radio_wave'}
]


def index(request):
    data = {'title': 'Главная страница',
            'menu': menu,
            'connectionType': connectionType,

            }
    logger.info('Index page accessed')
    return render(request, 'homework_1/index.html', context=data)


def about(request):
    logger.info('about page accessed')
    return render(request, 'homework_1/about.html', {'title': 'О сайте', 'menu': menu})


def optika(request):
    logger.info('optika page accessed')
    return render(request, 'homework_1/optika.html', {'title': 'Подключение по оптики', 'menu': menu})


def copper(request):
    logger.info('copper page accessed')
    return render(request, 'homework_1/copper.html', {'title': 'Подключение по меди', 'menu': menu})


def radio_wave(request):
    logger.info('radio_wave page accessed')
    return render(request, 'homework_1/radio_wave.html', {'title': 'Подключение по радиоволне', 'menu': menu})


# Домашнее задание № 2
def online_store(request):
    shop_menu = [
        {'title': 'Добавление клиента', 'url_name': 'create_client'},
        {'title': 'Изменение имени клиента', 'url_name': 'update_name_client'},
        {'title': 'Удаление клиента', 'url_name': 'delete_client'},
        {'title': 'Получение списка клиентов', 'url_name': 'get_client_all'},
        {'title': 'Получение списка продуктов', 'url_name': 'get_product_all'},
        {'title': 'Получение списка заказов', 'url_name': 'orders'},
        {'title': 'форма для выбора клиента и кол дней', 'url_name': 'get_product_client_day'},

    ]
    data = {'title': 'Интернет магазин',
            'menu': menu,
            'shop_menu': shop_menu,
            }
    return render(request, 'homework_1/online_store.html', context=data)


# Вывод списка всех клиентов
def create_client(request):
    return render(request, 'homework_1/create_client.html', {'title': 'Добавление клиента', 'menu': menu})


def update_name_client(request):
    return render(request, 'homework_1/update_name_client.html', {'title': 'Изменение имени клиента', 'menu': menu})


# Вывод всех клиентов
def get_client_all(request):
    clients = Client.objects.all()
    logger.info(f'Страница "Список клиентов" успешно открыта')
    return render(request, 'homework_1/get_client_all.html',
                  {'title': 'Получение списка всех клиентов', 'menu': menu, 'clients': clients})


def delete_client(request):
    return render(request, 'homework_1/delete_client.html', {'title': 'Удаление клиента', 'menu': menu})


def client_products_sorted(request, id_client: int, days: int):
    products = []
    product_set = []
    now = datetime.now()
    before = now - timedelta(days=days)
    clienti = Client.objects.filter(pk=id_client).first()
    orders = Oder.objects.filter(client=clienti, date_order__range=(before, now)).all()
    for order in orders:
        products = order.product.all()
        for product in products:
            if product not in product_set:
                product_set.append(product)

    return render(request, 'homework_1/client_all_products_from_orders.html',
                  {'client': clienti, 'product_set': product_set, 'days': days})


# Вывод всех продуктов
def get_product_all(request):
    products = Product.objects.all()
    logger.info(f'Страница "Список продуктов" успешно открыта')
    return render(request, 'homework_1/get_product_all.html',
                  {'title': 'Получение списка всех продуктов', 'menu': menu, 'products': products})


# Вывод списка заказов
def orders(request):
    orders = Oder.objects.all()
    return render(request, 'homework_1/orders_all.html',
                  {'title': 'Получение списка всех заказов', 'menu': menu, 'orders': orders})


# форма для выбора клиента и кол дней
def get_product_client_day(request):
    if request.method == "POST":
        form = GetProductClientDays(request.POST, request.FILES)
        if form.is_valid():
            id_client = request.POST['id_client']
            days = request.POST['days']

            return redirect("client_products_sorted", id_client, days)
    else:
        form = GetProductClientDays()

    context = {
            'title': 'форма для выбора клиента и кол дней',
            'menu': menu,
            "form": form
        }

    return render(request, "homework_1/get_product_client_day.html", context=context)
