# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 05:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myuser', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='date_of_birth',
        ),
        migrations.AddField(
            model_name='myuser',
            name='last_name',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
    ]
