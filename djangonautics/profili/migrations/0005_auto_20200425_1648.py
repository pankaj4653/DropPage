# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-25 16:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profili', '0004_auto_20200425_1645'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='pofile',
            new_name='Profile',
        ),
    ]