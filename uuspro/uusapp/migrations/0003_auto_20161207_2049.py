# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-07 12:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uusapp', '0002_auto_20161206_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='img',
            name='title',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]