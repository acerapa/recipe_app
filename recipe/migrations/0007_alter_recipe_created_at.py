# Generated by Django 4.0.3 on 2022-03-16 10:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0006_rename_file_id_recipe_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 16, 18, 16, 35, 659274)),
        ),
    ]