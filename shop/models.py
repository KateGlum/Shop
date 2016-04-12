# -*- coding: utf-8 -*-
# !/usr/bin/env python3

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название категории')
    in_stock = models.IntegerField(default=0, verbose_name='Видов в наличии')
    alias = models.SlugField(verbose_name='Alias категории')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


SHORT_NAME_LEN = 35

class Item(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование товара')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Цена')
    description = models.TextField(verbose_name='Описание товара')
    alias = models.SlugField(verbose_name='Alias товара')
    image = models.ImageField(upload_to='media', blank=True, null=True, verbose_name='изображение')
    category = models.ForeignKey(Category, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_short_name(self):
        if len(self.name) > SHORT_NAME_LEN:
            return self.name[:SHORT_NAME_LEN]
        else:
            return self.name

    class Meta:
        ordering = ['-price', 'name']
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Zakaz(models.Model):
    name = models.CharField(max_length=255, verbose_name='ФИО')
    phone = models.CharField(max_length=255, verbose_name='Телефон')
    data_zakaza = models.DateTimeField(default=timezone.now, verbose_name='Дата заказа')
    zakaz = models.TextField(verbose_name='Товар в заказе')
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Общая сумма заказа')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class Annotation(models.Model):
    text = models.TextField(verbose_name='Отзыв')
    created_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    item_annot = models.ForeignKey(Item, related_name='comments', verbose_name='Товар')
    author = models.ForeignKey(User, blank=True, null=True, verbose_name='Имя')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
