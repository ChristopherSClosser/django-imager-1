# Generated by Django 2.0 on 2017-12-09 22:13

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('imager_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagerprofile',
            name='photo_style',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('BLACK&WHITE', 'Black and White'), ('COLOR', 'Color'), ('PHOTOSHOP', 'Photoshop')], max_length=27),
        ),
    ]