# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-19 13:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20180119_1240'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='category',
            field=models.CharField(choices=[('Math', 'Math'), ('Geography', 'Geography'), ('Biology', 'Biology'), ('Physics', 'Physics'), ('Chemistry', 'Chemistry'), ('Health', 'Health'), ('Computer Science', 'Computer Science'), ('History', 'History')], default=None, max_length=50),
        ),
    ]
