# Generated by Django 2.1.2 on 2019-10-26 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locationmodel',
            name='id',
            field=models.CharField(default='loc_2019102623235da18b8c9', max_length=30, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='stationmodel',
            name='id',
            field=models.CharField(default='sta_201910262323507526e51', max_length=30, primary_key=True, serialize=False, unique=True),
        ),
    ]
