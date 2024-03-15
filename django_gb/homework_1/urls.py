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
    path('get_product_all/', views.get_product_all, name='get_product_all'),  # Получение списка продуктов
    path('orders/', views.orders, name='orders'),  # Вывод списка заказов
    path('get_product_client_day/', views.get_product_client_day, name='get_product_client_day'),  # Выбора клиента и кол дней
    path('client_products_sorted/<int:id_client>/<int:days>/', views.client_products_sorted, name='client_products_sorted'),  # вывод всех товаров по клиенту за последние кол дней
    path('create_product/', views.create_product, name='create_product'),  # Добавление товара
    path('product/<int:id_product>', views.product, name='product'),  # вывод выбранного пользователем продукта
    path('product_form/<int:id_product>', views.product_form, name='product_form'),  # Форма для изменения продукта
    path('choice_product_id_form/', views.choice_product_by_id, name='choice_product_id_form'),  # форма для выбора id продукта
]
