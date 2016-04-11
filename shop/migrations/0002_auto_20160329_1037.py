# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='in_stock',
            field=models.IntegerField(default=0, verbose_name='Видов в наличии'),
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(null=True, upload_to='media', verbose_name='изображение', blank=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=2, verbose_name='Цена'),
        ),
    ]
