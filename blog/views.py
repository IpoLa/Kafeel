# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .form import SignUpForm
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
def login(request):
    if request.user.is_authenticated():
            form = SignUpForm()
            context = {
            "form" : form
            }
            return render(request, "hamovid.html",context)
    if not request.user.is_authenticated():
        form = SignUpForm()
        context = {
        "form" : form
        }
        return render(request, "login.html", context)
