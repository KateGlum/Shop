# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20160405_2020'),
    ]

    operations = [
        migrations.CreateModel(
            name='Annotation',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('text', models.TextField(verbose_name='Отзыв')),
                ('created_date', models.DateTimeField(verbose_name='Дата создания', default=django.utils.timezone.now)),
                ('item_annot', models.ForeignKey(verbose_name='Товар', to='shop.Item', related_name='comments')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
    ]
