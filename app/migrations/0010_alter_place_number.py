# Generated by Django 4.2.3 on 2023-08-13 18:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_movie_image_alter_movie_label_alter_movie_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='number',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(20), django.core.validators.MinValueValidator(0)]),
        ),
    ]
