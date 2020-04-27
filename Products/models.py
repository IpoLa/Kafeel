# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length = 120)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits = 20, decimal_places = 0, default=200)
    sale_price = models.DecimalField(max_digits = 20, decimal_places = 0, null=True, blank=True)
    # image = models.FileField(upload_to = 'Products/images/', null=True)
    slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title

        class Meta:
            unique_together = ('title', 'slug')

    def get_price(self):
        # if self.on_sale():
        return self.price

    def get_absolute_url(self):
        return reverse("single_product", kwargs={"slug": self.slug})

class ProductImage(models.Model):
    product = models.ForeignKey(Product)
    image = models.ImageField(upload_to='')
    featured = models.BooleanField(default=False)
    thumbnail = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.product.title
