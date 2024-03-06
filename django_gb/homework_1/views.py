from django.http import HttpResponse
from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)

menu = [
    {'title': 'Главная страница', 'url_name': 'home'},
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
