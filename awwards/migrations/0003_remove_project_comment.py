# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-06-06 10:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awwards', '0002_remove_profile_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='comment',
        ),
    ]
