# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-18 12:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20180118_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]
