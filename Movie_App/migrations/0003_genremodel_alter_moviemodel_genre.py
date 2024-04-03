# Generated by Django 5.0 on 2024-04-03 06:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movie_App', '0002_alter_moviemodel_genre_alter_moviemodel_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='GenreModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='moviemodel',
            name='genre',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Movie_App.genremodel'),
        ),
    ]