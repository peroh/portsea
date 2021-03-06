# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-13 02:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=128)),
                ('course_start_date', models.DateField(blank=True, null=True)),
                ('course_end_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CourseType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_type', models.CharField(max_length=128)),
                ('paperwork_template', models.FileField(blank=True, upload_to='paperwork_templates')),
            ],
        ),
        migrations.CreateModel(
            name='PaperworkHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paperwork', models.FileField(upload_to=b'')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='course_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.CourseType'),
        ),
    ]
