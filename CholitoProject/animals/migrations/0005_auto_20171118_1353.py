# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-18 16:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0004_auto_20171118_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='first_day',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
