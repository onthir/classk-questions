# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-28 03:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20180128_0245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='category',
            field=models.CharField(choices=[('Math', 'Math'), ('Geography', 'Geography'), ('Biology', 'Biology'), ('Physics', 'Physics'), ('Chemistry', 'Chemistry'), ('Health', 'Health'), ('Computer-Science', 'Computer-Science'), ('History', 'History')], default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 28, 3, 23, 34, 757134), null=True),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
