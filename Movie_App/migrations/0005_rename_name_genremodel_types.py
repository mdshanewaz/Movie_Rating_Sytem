# Generated by Django 5.0 on 2024-04-03 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Movie_App', '0004_remove_moviemodel_genre'),
    ]

    operations = [
        migrations.RenameField(
            model_name='genremodel',
            old_name='name',
            new_name='types',
        ),
    ]
