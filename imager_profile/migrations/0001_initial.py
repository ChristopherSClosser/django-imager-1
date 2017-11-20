# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-20 22:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website', models.CharField(blank=True, max_length=150, null=True)),
                ('location', models.CharField(blank=True, max_length=200, null=True)),
                ('fee', models.FloatField(blank=True, max_length=6, null=True)),
                ('camera', models.CharField(choices=[('SLR', 'SLR'), ('Range finder', 'Range finder'), ('Twin reflex', 'Twin reflex')], max_length=15)),
                ('services', models.CharField(choices=[('WEDDING', 'Wedding'), ('PAPARAZZI', 'Paparazzi')], max_length=20)),
                ('bio', models.TextField(blank=True, max_length=200, null=True)),
                ('phone', models.CharField(blank=True, max_length=11, null=True)),
                ('photo_style', models.CharField(choices=[('BLACK AND WHITE', 'Black and White'), ('COLOR', 'Color'), ('PHOTOSHOP', 'Photoshop')], max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
