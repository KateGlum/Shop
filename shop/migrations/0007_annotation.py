# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0006_auto_20160405_2020'),
    ]

    operations = [
        migrations.CreateModel(
            name='Annotation',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('text', models.TextField(verbose_name='Отзыв')),
                ('created_date', models.DateTimeField(verbose_name='Дата создания', default=django.utils.timezone.now)),
                ('approved_annot', models.BooleanField(verbose_name='Подтверждение', default=False)),
                ('annot_author', models.ForeignKey(verbose_name='Имя', to=settings.AUTH_USER_MODEL)),
                ('item_annot', models.ForeignKey(verbose_name='Товар', related_name='comments', to='shop.Item')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
    ]
