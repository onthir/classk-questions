# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-28 02:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20180127_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='posted_on',
            field=models.DateField(default=datetime.date(2018, 1, 28)),
        ),
    ]
