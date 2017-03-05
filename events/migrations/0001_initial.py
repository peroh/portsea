# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-15 05:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('start_time', models.TimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('end_time', models.TimeField(blank=True, default=django.utils.timezone.now, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EventSignup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('start_time', models.TimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('end_time', models.TimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='member_signup',
            field=models.ManyToManyField(through='events.EventSignup', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='event',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.EventType'),
        ),
    ]