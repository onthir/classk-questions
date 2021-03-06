# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-04 13:51
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0035_auto_20180203_0835'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('any_message', models.CharField(default='Notification', max_length=500, null=True)),
                ('read', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='answer',
            name='posted_on',
            field=models.DateField(default=datetime.date(2018, 2, 4)),
        ),
        migrations.AlterField(
            model_name='question',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 4, 13, 51, 14, 379296, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(default='Short title of your problem', max_length=150),
        ),
        migrations.AddField(
            model_name='notification',
            name='answer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Answer'),
        ),
        migrations.AddField(
            model_name='notification',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Question'),
        ),
        migrations.AddField(
            model_name='notification',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
