# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-04 19:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imager_profile', '0004_auto_20171204_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagerprofile',
            name='phone',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]