# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-08 19:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ice_cream', '0006_auto_20160608_1857'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flavorimage',
            name='flavor',
        ),
        migrations.AddField(
            model_name='flavor',
            name='image',
            field=models.ImageField(default=1, upload_to='static/flavor_pics'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='FlavorImage',
        ),
    ]