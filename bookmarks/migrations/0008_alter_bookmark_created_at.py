# Generated by Django 4.0.3 on 2022-05-26 10:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarks', '0007_alter_bookmark_created_at_alter_bookmark_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 26, 18, 15, 18, 607587)),
        ),
    ]
