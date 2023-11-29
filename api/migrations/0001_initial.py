# Generated by Django 4.2.7 on 2023-11-29 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='название товара')),
                ('description', models.TextField(blank=True, verbose_name='описание товара')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='цена товара')),
            ],
        ),
    ]
