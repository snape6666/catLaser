# Generated by Django 2.1.4 on 2019-01-21 23:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_auto_20190122_0040'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Point3D',
            new_name='LaserPosition',
        ),
    ]