# Generated by Django 4.0.3 on 2022-03-16 10:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0005_alter_file_created_at_alter_file_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 16, 18, 12, 4, 853947)),
        ),
    ]