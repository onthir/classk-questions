# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-01 03:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_auto_20180201_0323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 1, 3, 47, 50, 111716, tzinfo=utc), null=True),
        ),
    ]
