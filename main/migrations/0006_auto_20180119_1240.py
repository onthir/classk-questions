# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-19 12:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20180119_1238'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='date',
        ),
        migrations.AddField(
            model_name='answer',
            name='posted_on',
            field=models.DateField(default=datetime.date(2018, 1, 19)),
        ),
    ]
