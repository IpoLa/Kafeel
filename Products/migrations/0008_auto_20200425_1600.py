# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-25 16:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0007_auto_20200425_0053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(null=True, upload_to='static/media/image'),
        ),
    ]
