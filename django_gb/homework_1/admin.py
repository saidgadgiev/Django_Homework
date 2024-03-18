from django.contrib import admin
from .models import Client, Product, Oder


@admin.action(description='Сбросить количество в ноль')
def reset_quantity_product(modeladmin, request, queryset):
    queryset.update(quantity_product=0)


class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'email']
    ordering = ['name']
    search_fields = ['name']
    search_help_text = 'Поиск по имени (description)'

    readonly_fields = ['date_registration']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'cost', 'quantity_product']
    actions = [reset_quantity_product]
    ordering = ['-quantity_product']
    list_filter = ['data_add', 'cost']
    search_fields = ['product_name']
    search_help_text = 'Поиск названию продукта (description)'

    """Отдельный продукт."""
    # fields = ['product_name', 'cost', 'quantity_product', 'product_description']
    readonly_fields = ['product_image']

    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['product_name'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Категория товара и его подробное описание',
                'fields': ['product_description'],
            },
        ),
        (
            'Бухгалтерия',
            {
                'fields': ['cost', 'quantity_product'],
            }
        ),

    ]


class OderAdmin(admin.ModelAdmin):
    list_display = ['client', 'order_summ']
    readonly_fields = ['date_order']


admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Oder, OderAdmin)

