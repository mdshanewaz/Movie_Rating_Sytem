# Generated by Django 5.0 on 2024-04-03 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Movie_App', '0009_moviemodel_ratingmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='moviemodel',
            old_name='RatingModel',
            new_name='rating',
        ),
    ]
