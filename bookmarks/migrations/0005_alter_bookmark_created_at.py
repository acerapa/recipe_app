# Generated by Django 4.0.3 on 2022-03-16 10:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarks', '0004_alter_bookmark_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 16, 18, 16, 35, 661272)),
        ),
    ]
