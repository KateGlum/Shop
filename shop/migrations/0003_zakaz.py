# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20160329_1037'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zakaz',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(verbose_name='Имя заказчика', max_length=255)),
                ('phone', models.CharField(verbose_name='Телефон заказчика', max_length=255)),
                ('zakaz', models.CharField(verbose_name='Заказ', max_length=255)),
                ('summa', models.DecimalField(max_digits=10, verbose_name='Сумма заказа', decimal_places=2, default=0)),
                ('data_zakaza', models.DateTimeField(verbose_name='Дата заказа', default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': 'Заказы',
                'verbose_name': 'Заказ',
            },
        ),
    ]
