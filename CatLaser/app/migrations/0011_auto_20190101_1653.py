# Generated by Django 2.1.4 on 2019-01-01 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20190101_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='point',
            name='x',
            field=models.IntegerField(verbose_name='X-Value'),
        ),
        migrations.AlterField(
            model_name='point',
            name='y',
            field=models.IntegerField(verbose_name='Y-Value'),
        ),
    ]
