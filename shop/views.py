# -*- coding: utf-8 -*-
# !/usr/bin/env python3

from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.template.context_processors import csrf
from django.views.generic.edit import FormView
from shop.form import ZakazForm, AnnotationForm
from shop.models import Item, Category, Annotation
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator
from random import randrange


def main(request, page_number=1):
    items = Item.objects.all()
    current_page = Paginator(items, 9)
    return render(request, 'shop/shop.html', {'items': current_page.page(page_number)})


def contact(request):
    return render(request, 'shop/contact.html')


def show_item(request, item_id):
    form = AnnotationForm
    args = {}
    args.update(csrf(request))
    args['item'] = get_object_or_404(Item, id=item_id)
    args['comments'] = Annotation.objects.filter(item_annot_id=item_id)
    args['form'] = form
    args['username'] = auth.get_user(request).username
    return render(request, 'shop/item.html', args)


@login_required(login_url='/accounts/login/')
def add_comment(request, item_id):
    if request.POST:
        form = AnnotationForm(request.POST, 'user')
        if form.is_valid():
            annotation = form.save(commit=False)
            annotation.author = request.user
            annotation.item_annot = Item.objects.get(id=item_id)
            form.save()

    return redirect('/items/%s' % item_id)


def register(request):
    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm()
    if request.POST:
        newuser_form = UserCreationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = auth.authenticate(username=newuser_form.cleaned_data['username'],
                                        password=newuser_form.cleaned_data['password2'])
            auth.login(request, newuser)
            return redirect('/')
        else:
            args['form'] = newuser_form
    return render_to_response('registration/register.html', args)


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