# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20160405_1844'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zakaz',
            name='is_closed',
        ),
        migrations.RemoveField(
            model_name='zakaz',
            name='is_processed',
        ),
        migrations.AddField(
            model_name='zakaz',
            name='total',
            field=models.DecimalField(verbose_name='Общая сумма заказа', default=0, max_digits=10, decimal_places=2),
        ),
        migrations.AddField(
            model_name='zakaz',
            name='zakaz',
            field=models.TextField(verbose_name='Товар в заказе', default=datetime.datetime(2016, 4, 5, 17, 20, 48, 576427, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
