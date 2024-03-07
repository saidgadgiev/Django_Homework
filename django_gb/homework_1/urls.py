from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),  # http://127.0.0.1:8000/
    path('about/', views.about, name='about'),  # http://127.0.0.1:8000/about/
    path('optika/', views.optika, name='optika'),  # оптика
    path('copper/', views.copper, name='copper'),  # медь
    path('radio_wave/', views.radio_wave, name='radio_wave'),  # радиоволна
    path('online_store/', views.online_store, name='online_store'),  # Интернет магазин
    path('create_client/', views.create_client, name='create_client'),  # Добавление клиента
    path('update_name_client/', views.update_name_client, name='update_name_client'),  # Изменение имени клиента
    path('get_client_all/', views.get_client_all, name='get_client_all'),  # Получение списка клиентов
    path('delete_client/', views.delete_client, name='delete_client'),  # Удаление клиента
]
