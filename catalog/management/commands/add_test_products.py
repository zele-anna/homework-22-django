from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Add test products'

    def handle(self, *args, **options):

        # Удаление существующих записей
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Добавление тестовых данных
        category, _ = Category.objects.get_or_create(name='Тест', description='Для проверки')

        test_products = [
            {'name': 'Тест 1', 'description': 'Описание тест 1', 'category': category, 'price': '1000', 'created_at': '2010-01-01', 'updated_at': '2020-06-07'},
            {'name': 'Тест 2', 'description': 'Описание тест 2', 'category': category, 'price': '2000',
             'created_at': '2010-01-01', 'updated_at': '2020-06-07'},
            {'name': 'Тест 3', 'description': 'Описание тест 3', 'category': category, 'price': '3000',
             'created_at': '2010-01-01', 'updated_at': '2020-06-07'},
        ]

        for product_data in test_products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Продукт {product.name} успешно добавлен!'))
            else:
                self.stdout.write(self.style.WARNING(f'Продукт {product.name} уже создан.'))
