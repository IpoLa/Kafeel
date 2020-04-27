# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .form import SignUpForm
from Products.models import Product
# Create your views here.
# def login(request):
#     # title = "Hello guest !"
#     if request.user.is_authenticated():
#         title = "Hello %s" %(request.user)
#     form = SignUpForm()
#     context = {
#         "template_title" : title,
#         "form" : form
    # }
    # return render(request, "login.html", context)


# def single(request, slug):
#     try:
#         product = Product.objects.get(slug=slug)
#         print product.title
#         context = {
#         'product' : product
#         }
#         template = 'products/single.html'
#         return render(request, template, context)
#     except:
#         raise Http404



def login(request):
    # if request.user.is_authenticated():
            products = Product.objects.all()
            # form = SignUpForm()
            context = {
            # "form" : form,
            "products" : products
            # "username_is" : request.user
            }
            template = 'login.html'
            return render(request, template, context)
    # else:
        # form = SignUpForm()
        # context = {
        # "form" : form,
        # }
        # template = 'login.html'
        # return render(request, template, context)

def home(request):

    template = 'hamovid.html'
    context = {
    "username_is" : request.user
    }
    return render(request, template, context)


# def single(request, slug):
#     print slug
#     product = Product.objects.get(slug=slug)
#     products = Product.objects.all()
#     context = {
#     'products' : products
#     }
#     template = 'all.html'
#     return render(request, template, context)

# def all(request):
#     products = Product.objects.all()
#     context = {
#     'products' : products
#     }
#     template = 'all.html'
#     return render(request, template, context)
