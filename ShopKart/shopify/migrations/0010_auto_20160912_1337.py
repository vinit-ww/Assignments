# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-12 08:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopify', '0009_auto_20160912_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='map',
            name='brands',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopify.Brand'),
        ),
    ]
