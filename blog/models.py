# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class SignUp(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length = 30, blank = False, null = True)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
    updated = models.DateTimeField(auto_now_add = True, auto_now = False)
    def _unicode_(self):
        return self.email

# class Product(models.Model):
#     title = models.CharField(max_length = 120)
#     description = models.TextField()
#     price = models.DecimalField(max_digits = 20, decimal_places = 0)
#     slug = models.SlugField()
#     timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
#     updated = models.DateTimeField(auto_now_add=False, auto_now=True)
#     active = models.BooleanField(default=True)
#
#     def __unicode__(self):
#         return self.title
