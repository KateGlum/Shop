# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20160405_1321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zakazposition',
            name='item',
        ),
        migrations.RemoveField(
            model_name='zakazposition',
            name='zakaz',
        ),
        migrations.DeleteModel(
            name='ZakazPosition',
        ),
    ]
