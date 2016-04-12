# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0007_annotation'),
    ]

    operations = [
        migrations.AddField(
            model_name='annotation',
            name='author',
            field=models.ForeignKey(default=1, verbose_name='Имя', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
