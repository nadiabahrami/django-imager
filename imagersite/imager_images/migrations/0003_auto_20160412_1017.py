# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-12 17:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imager_images', '0002_auto_20160411_1754'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='owner',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='photo',
            old_name='owner',
            new_name='user',
        ),
    ]