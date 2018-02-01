# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-01 04:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_auto_20180201_0347'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='irrelevant',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='question',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 1, 4, 25, 31, 928388, tzinfo=utc), null=True),
        ),
    ]
