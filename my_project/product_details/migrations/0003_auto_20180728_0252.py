# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-28 02:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_details', '0002_auto_20180728_0247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=1000),
        ),
    ]
