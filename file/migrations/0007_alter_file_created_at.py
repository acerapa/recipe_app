# Generated by Django 4.0.3 on 2022-03-16 10:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0006_alter_file_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 16, 18, 15, 17, 986062)),
        ),
    ]