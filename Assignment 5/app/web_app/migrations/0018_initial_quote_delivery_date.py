# Generated by Django 4.0.2 on 2022-05-06 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0017_initial_quote'),
    ]

    operations = [
        migrations.AddField(
            model_name='initial_quote',
            name='delivery_date',
            field=models.DateField(null=True),
        ),
    ]
