# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-01 21:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('X_Home', '0009_auto_20161002_0249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='summary',
            field=models.CharField(default='Nothing to show', max_length=300, null=True),
        ),
    ]
