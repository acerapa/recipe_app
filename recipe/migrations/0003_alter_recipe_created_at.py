# Generated by Django 4.0.3 on 2022-03-14 03:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_alter_recipe_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 14, 11, 20, 27, 954890)),
        ),
    ]