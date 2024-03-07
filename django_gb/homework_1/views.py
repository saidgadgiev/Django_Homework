from django.http import HttpResponse
from django.shortcuts import render
import logging

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
        {'title': 'Получение списка клиентов', 'url_name': 'get_client_all'}
    ]
    data = {'title': 'Интернет магазин',
            'menu': menu,
            'shop_menu': shop_menu,
            }
    return render(request, 'homework_1/online_store.html', context=data)


def create_client(request):
    return render(request, 'homework_1/create_client.html', {'title': 'Добавление клиента', 'menu': menu})


def update_name_client(request):
    return render(request, 'homework_1/update_name_client.html', {'title': 'Изменение имени клиента', 'menu': menu})


def get_client_all(request):
    return render(request, 'homework_1/get_client_all.html', {'title': 'Получение списка клиентов', 'menu': menu})


def delete_client(request):
    return render(request, 'homework_1/delete_client.html', {'title': 'Удаление клиента', 'menu': menu})