# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 18:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20171027_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopping',
            name='invoice_id',
            field=models.CharField(max_length=32),
        ),
    ]