# Generated by Django 4.0.3 on 2022-03-25 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0011_alter_file_created_at'),
        ('account', '0004_alter_account_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='file',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='file.file'),
        ),
    ]