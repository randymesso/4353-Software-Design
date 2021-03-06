# Generated by Django 4.0.2 on 2022-05-06 19:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0019_remove_initial_quote_suggested_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='initial_quote',
            name='suggested_price',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='initial_quote',
            name='total_due',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
