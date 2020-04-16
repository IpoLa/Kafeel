# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import SignUp
# from .form import SignUpForm

class SignUpAdmin(admin.ModelAdmin):
    list_display = ["_unicode_", "full_name", "timestamp", "updated"]
    # form = SignUpForm
    class Meta:
        model = SignUp

admin.site.register(SignUp, SignUpAdmin)
