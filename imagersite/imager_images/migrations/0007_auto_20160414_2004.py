# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-15 03:04
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('imager_images', '0006_auto_20160412_1935'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='album',
            managers=[
                ('all_albums', django.db.models.manager.Manager()),
            ],
        ),
    ]
