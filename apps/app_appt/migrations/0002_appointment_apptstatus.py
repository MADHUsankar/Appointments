# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-28 22:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app_appt', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='apptstatus',
            field=models.CharField(default=django.utils.timezone.now, max_length=38),
            preserve_default=False,
        ),
    ]