# Generated by Django 5.0 on 2024-04-03 10:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movie_App', '0012_remove_moviemodel_rating'),
        ('Rating_App', '0004_delete_ratingmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviemodel',
            name='rating',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='Rating_App.ratemodel'),
        ),
    ]
