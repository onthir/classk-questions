# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-19 12:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_auto_20180119_1139'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.IntegerField(default=None, null=True),
        ),
    ]
