# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-20 02:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20180120_0240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer',
            field=models.TextField(max_length=3000, null=True),
        ),
    ]
