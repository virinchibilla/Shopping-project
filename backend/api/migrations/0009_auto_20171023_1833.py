# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-23 18:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_apiuser_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apiuser',
            old_name='user_name',
            new_name='username',
        ),
    ]
