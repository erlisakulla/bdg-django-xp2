# Generated by Django 3.1.7 on 2021-03-16 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_auto_20210314_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='downstream_player',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='role',
            name='upstream_player',
            field=models.IntegerField(default=0),
        ),
    ]
