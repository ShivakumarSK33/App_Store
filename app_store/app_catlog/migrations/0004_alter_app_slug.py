# Generated by Django 5.1 on 2024-10-07 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_catlog', '0003_app_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='slug',
            field=models.SlugField(default='', unique=True),
        ),
    ]
