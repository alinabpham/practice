# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-06 21:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ice_cream', '0003_options'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Options',
            new_name='Option',
        ),
    ]