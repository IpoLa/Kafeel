# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-25 00:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0006_auto_20200425_0029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
