# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-06-06 12:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awwards', '0004_auto_20200606_1121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='creativity',
        ),
    ]
