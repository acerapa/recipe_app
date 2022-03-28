# Generated by Django 4.0.3 on 2022-03-16 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0008_alter_file_created_at'),
        ('account', '0002_alter_account_options_alter_account_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='file_id',
        ),
        migrations.AddField(
            model_name='account',
            name='file',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='file.file'),
        ),
    ]