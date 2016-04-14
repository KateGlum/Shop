# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_annotation_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annotation',
            name='author',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='Имя', null=True),
        ),
    ]
