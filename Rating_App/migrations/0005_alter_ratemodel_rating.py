# Generated by Django 5.0 on 2024-04-03 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rating_App', '0004_delete_ratingmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratemodel',
            name='rating',
            field=models.FloatField(max_length=10, null=True),
        ),
    ]