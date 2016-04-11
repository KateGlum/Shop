# -*- coding: utf-8 -*-
# !/usr/bin/env python3

from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.template.context_processors import csrf
from django.views.generic.edit import FormView
from shop.form import ZakazForm
from shop.models import Item, Category
from django.http import Http404, HttpResponse
from django.utils import timezone
from django.core.paginator import Paginator


def main(request, page_number=1):
    items = Item.objects.all()
    current_page = Paginator(items, 9)
    return render(request, 'shop/shop.html', {'items': current_page.page(page_number)})


def contact(request):
    return render(request, 'shop/contact.html')


def show_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    return render(request, 'shop/item.html', {'item': item})


def show_category(request, alias):
    try:
        category = Category.objects.get(alias=alias)
        items = Item.objects.filter(category=category)
    except:
        raise Http404('Объект не найден')
    context = {
        'items': items,
        'category': category,
    }
    return render(request, 'shop/category.html', context)


def cart(request):
    return render(request, 'shop/cart.html')


class OformitZakaz(FormView):
    form_class = ZakazForm
    success_url = '/contact/'
    template_name = 'shop/oformit_zakaz.html'

    def form_valid(self, form):
        form.save()
        return super(OformitZakaz, self).form_valid(form)


def search(request):
    query = request.GET.get('q', '')
    results = []
    if query:
        results = Item.objects.filter(name__icontains=query)
    return render_to_response('shop/search.html',
                              {'query': query,
                               'results': results})