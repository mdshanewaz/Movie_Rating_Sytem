# Generated by Django 5.0 on 2024-04-03 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rating_App', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ratingmodel',
            name='rate_points',
        ),
        migrations.AddField(
            model_name='ratingmodel',
            name='rating',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
