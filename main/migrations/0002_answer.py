# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-19 12:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(max_length=3000)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Question')),
            ],
        ),
    ]
