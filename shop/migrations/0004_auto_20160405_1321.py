# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_zakaz'),
    ]

    operations = [
        migrations.CreateModel(
            name='ZakazPosition',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('count', models.PositiveIntegerField(default=0)),
                ('item', models.ForeignKey(to='shop.Item')),
            ],
            options={
                'ordering': ['-count'],
                'verbose_name_plural': 'Позиции заказа',
                'verbose_name': 'Позиция заказа',
            },
        ),
        migrations.RemoveField(
            model_name='zakaz',
            name='summa',
        ),
        migrations.RemoveField(
            model_name='zakaz',
            name='zakaz',
        ),
        migrations.AddField(
            model_name='zakaz',
            name='is_closed',
            field=models.BooleanField(default=False, verbose_name='Закрыт'),
        ),
        migrations.AddField(
            model_name='zakaz',
            name='is_processed',
            field=models.BooleanField(default=False, verbose_name='В процессе'),
        ),
        migrations.AlterField(
            model_name='zakaz',
            name='name',
            field=models.CharField(max_length=255, verbose_name='ФИО'),
        ),
        migrations.AlterField(
            model_name='zakaz',
            name='phone',
            field=models.CharField(max_length=255, verbose_name='Телефон'),
        ),
        migrations.AddField(
            model_name='zakazposition',
            name='zakaz',
            field=models.ForeignKey(to='shop.Zakaz', related_name='positions'),
        ),
    ]
