# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-30 23:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('job', models.CharField(max_length=300)),
                ('department', models.CharField(max_length=300)),
                ('salary', models.CharField(max_length=300)),
                ('salary2', models.CharField(max_length=300)),
            ],
        ),
    ]
