# Generated by Django 4.2.3 on 2023-08-13 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_place_number'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Place',
        ),
    ]