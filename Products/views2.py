# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import Product, ProductImage
# Create your views here.

def dashboard(request):
    products = Product.objects.all()
    context = {
    "products" : products
    }
    template = 'home.html'
    return render(request, template, context)


def search(request):
    try:
        q = request.GET.get('q')
    except:
        q = None
    if q:
        products = Product.objects.filter(title__icontains=q)
        context = {'query' : q, "products" : products}
        template = 'results.html'
    else:
        template = 'home.html'
        context = {}
    return render(request, template, context)


def all(request):
    products = Product.objects.all()
    context = {
    'products' : products
    }
    template = 'all.html'
    return render(request, template, context)

def single(request, slug):
    try:
        product = Product.objects.get(slug=slug)
        # images = product.objects.productimage_set.all()
        images = ProductImage.objects.filter(product=product)
        context = {'product' : product, "images": images}
        template = 'single.html'
        return render(request, template, context)
    except:
        raise Http404
