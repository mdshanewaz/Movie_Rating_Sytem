# Generated by Django 5.0 on 2024-04-03 07:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movie_App', '0006_remove_genremodel_types_genremodel_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviemodel',
            name='genre',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='Movie_App.genremodel'),
        ),
    ]