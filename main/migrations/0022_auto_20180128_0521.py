# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-28 05:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20180128_0326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 28, 5, 21, 26, 344426, tzinfo=utc), null=True),
        ),
    ]
