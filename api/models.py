from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=255, verbose_name='название товара')
    description = models.TextField(blank=True, verbose_name='описание товара')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена товара')

    def __str__(self):
        return f'Product {self.name} with price {self.price}'
