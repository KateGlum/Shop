# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='Название категории')),
                ('in_stock', models.IntegerField(verbose_name='В наличии', default=0)),
                ('alias', models.SlugField(verbose_name='Alias категории')),
            ],
            options={
                'verbose_name_plural': 'Категории',
                'verbose_name': 'Категория',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='Наименование товара')),
                ('price', models.FloatField(verbose_name='Цена', default=0)),
                ('description', models.TextField(verbose_name='Описание товара')),
                ('alias', models.SlugField(verbose_name='Alias товара')),
                ('image', models.CharField(max_length=255, verbose_name='Ссылка')),
                ('category', models.ForeignKey(null=True, blank=True, to='shop.Category')),
            ],
            options={
                'verbose_name_plural': 'Товары',
                'verbose_name': 'Товар',
                'ordering': ['-price', 'name'],
            },
        ),
    ]
