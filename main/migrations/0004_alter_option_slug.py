# Generated by Django 5.1 on 2024-09-05 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_option_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='option',
            name='slug',
            field=models.SlugField(blank=True, default=1, unique=True),
            preserve_default=False,
        ),
    ]
