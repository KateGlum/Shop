# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20160414_1734'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='Валюта', max_length=255)),
                ('rate', models.FloatField(verbose_name='Курс', default=0)),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
            },
        ),
        migrations.CreateModel(
            name='ItemForeign',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='Наименование товара', max_length=255)),
                ('price', models.DecimalField(verbose_name='Цена', decimal_places=2, default=0, max_digits=10)),
                ('description', models.TextField(verbose_name='Описание товара')),
                ('alias', models.SlugField(verbose_name='Alias товара')),
                ('image', models.ImageField(verbose_name='изображение', null=True, blank=True, upload_to='media')),
                ('rate', models.FloatField(verbose_name='Курс', default=0)),
                ('category', models.ForeignKey(null=True, to='shop.Category', blank=True)),
                ('currency', models.ForeignKey(to='shop.Currency')),
            ],
            options={
                'verbose_name': 'Товар_импорт',
                'verbose_name_plural': 'Товары_импорт',
                'ordering': ['-price', 'name'],
            },
        ),
    ]
