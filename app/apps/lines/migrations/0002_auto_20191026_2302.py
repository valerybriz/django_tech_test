# Generated by Django 2.1.2 on 2019-10-26 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lines', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linemodel',
            name='id',
            field=models.CharField(default='line_2019102623235e601d0c1', max_length=30, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='routemodel',
            name='id',
            field=models.CharField(default='route_2019102623235f4f8ff88', max_length=30, primary_key=True, serialize=False, unique=True),
        ),
    ]
