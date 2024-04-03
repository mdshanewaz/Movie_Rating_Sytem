# Generated by Django 5.0 on 2024-04-03 10:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movie_App', '0015_moviemodel_genre_moviemodel_name_moviemodel_rating_and_more'),
        ('Rating_App', '0006_alter_ratemodel_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviemodel',
            name='rating',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Rating_App.ratemodel'),
        ),
    ]
