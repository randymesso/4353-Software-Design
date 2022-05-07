# Generated by Django 4.0.2 on 2022-05-06 19:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0014_initial_quote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fuel_quote',
            name='gallons_requested',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]