# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-25 16:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0010_auto_20200425_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(upload_to='media/static/images/'),
        ),
    ]
