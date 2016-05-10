# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_currency_itemforeign'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='rate',
            field=models.DecimalField(verbose_name='Курс', max_digits=10, default=0, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='itemforeign',
            name='currency',
            field=models.ForeignKey(to='shop.Currency', blank=True),
        ),
        migrations.AlterField(
            model_name='itemforeign',
            name='rate',
            field=models.DecimalField(verbose_name='Курс', max_digits=10, default=0, decimal_places=2),
        ),
    ]
