# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-28 12:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_auto_20180128_0521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 28, 12, 0, 25, 66823, tzinfo=utc), null=True),
        ),
    ]
