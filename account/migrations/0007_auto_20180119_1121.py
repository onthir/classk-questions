# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-19 11:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20180119_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(default=None, max_length=100, null=True),
        ),
    ]
