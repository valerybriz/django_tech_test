# Generated by Django 2.1.2 on 2019-10-27 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0002_auto_20191026_2302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='locationmodel',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='locationmodel',
            name='longitude',
        ),
        migrations.AddField(
            model_name='locationmodel',
            name='coordinates',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='locationmodel',
            name='id',
            field=models.CharField(default='loc_20191027163419dddca5fb', max_length=30, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='stationmodel',
            name='id',
            field=models.CharField(default='sta_2019102716341907465e8b', max_length=30, primary_key=True, serialize=False, unique=True),
        ),
    ]
