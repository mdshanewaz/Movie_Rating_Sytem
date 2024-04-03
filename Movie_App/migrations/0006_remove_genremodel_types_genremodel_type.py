# Generated by Django 5.0 on 2024-04-03 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movie_App', '0005_rename_name_genremodel_types'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genremodel',
            name='types',
        ),
        migrations.AddField(
            model_name='genremodel',
            name='type',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
