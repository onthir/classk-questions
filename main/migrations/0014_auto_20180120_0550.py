# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-20 05:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20180120_0549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='date',
            field=models.DateField(default=datetime.date.today, null=True),
        ),
    ]
