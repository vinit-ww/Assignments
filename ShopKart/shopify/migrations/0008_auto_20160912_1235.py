# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-12 07:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopify', '0007_brand'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='brand_id',
        ),
        migrations.AddField(
            model_name='product',
            name='brands',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shopify.brand'),
            preserve_default=False,
        ),
    ]
