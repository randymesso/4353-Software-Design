# Generated by Django 4.0.2 on 2022-05-06 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0018_initial_quote_delivery_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='initial_quote',
            name='suggested_price',
        ),
        migrations.RemoveField(
            model_name='initial_quote',
            name='total_due',
        ),
    ]
