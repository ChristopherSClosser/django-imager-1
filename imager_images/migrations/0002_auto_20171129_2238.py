# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-29 22:38
from __future__ import unicode_literals

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('imager_images', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='cover',
            field=sorl.thumbnail.fields.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image_file',
            field=sorl.thumbnail.fields.ImageField(upload_to='django_imager/MEDIA'),
        ),
    ]
