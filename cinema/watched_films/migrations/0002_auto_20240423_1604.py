# Generated by Django 3.2.16 on 2024-04-23 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watched_films', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='add_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='originaltitle',
            name='add_time',
            field=models.DateTimeField(auto_created=True, null=True),
        ),
        migrations.AddField(
            model_name='watchedfilms',
            name='add_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]