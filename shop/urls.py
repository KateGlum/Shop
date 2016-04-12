# -*- coding: utf-8 -*-
# !/usr/bin/env python3

from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^items/(?P<item_id>[0-999]+)/$', views.show_item, name='item'),
    url(r'^items/add_comment/(?P<item_id>[0-999]+)/$', views.add_comment),
    url(r'^cart/$', views.cart, name='cart'),
    url(r'^zakaz/$', views.OformitZakaz.as_view(), name='zakaz'),
    url(r'^page/(\d+)/$', views.main),
    url(r'^search/$', views.search),
    url(r'^(?P<alias>[^/]+)/$', views.show_category, name='category'),
]

