# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 22:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20170222_2232'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventsignup',
            old_name='end_time',
            new_name='signup_time',
        ),
        migrations.RemoveField(
            model_name='eventsignup',
            name='start_time',
        ),
    ]
