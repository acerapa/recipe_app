# Generated by Django 4.0.3 on 2022-03-28 01:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('procedure', '0006_alter_procedure_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='procedure',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 28, 9, 22, 51, 750093)),
        ),
        migrations.AlterModelTable(
            name='procedure',
            table=None,
        ),
    ]