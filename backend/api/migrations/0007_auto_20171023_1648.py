# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-23 16:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20171023_1409'),
    ]

    operations = [
        migrations.AddField(
            model_name='apiuser',
            name='user_name',
            field=models.CharField(default='', max_length=120, unique=True),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='apiuser',
            name='address',
        ),
        migrations.AddField(
            model_name='apiuser',
            name='address',
            field=models.ManyToManyField(blank=True, to='api.Address'),
        ),
    ]
