# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-25 16:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profili', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='gender',
        ),
    ]
