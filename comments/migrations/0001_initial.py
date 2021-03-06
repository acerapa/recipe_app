# Generated by Django 4.0.3 on 2022-03-14 03:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('recipe', '0003_alter_recipe_created_at'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_id', models.IntegerField()),
                ('is_reply', models.BooleanField(default=False)),
                ('content', models.TextField()),
                ('likes', models.IntegerField()),
                ('dislikes', models.IntegerField()),
                ('recipe_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.recipe')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
