# Generated by Django 5.0 on 2024-04-03 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Movie_App', '0007_moviemodel_genre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moviemodel',
            name='rating',
        ),
    ]
