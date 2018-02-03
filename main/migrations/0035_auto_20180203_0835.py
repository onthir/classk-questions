# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-03 02:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0034_auto_20180203_0813'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='cat',
            new_name='category',
        ),
        migrations.AlterField(
            model_name='question',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 3, 2, 50, 24, 739598, tzinfo=utc), null=True),
        ),
    ]
