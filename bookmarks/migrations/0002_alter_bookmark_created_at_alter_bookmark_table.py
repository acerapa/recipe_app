# Generated by Django 4.0.3 on 2022-03-14 03:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 14, 11, 28, 58, 905703)),
        ),
        migrations.AlterModelTable(
            name='bookmark',
            table='bookmarks',
        ),
    ]