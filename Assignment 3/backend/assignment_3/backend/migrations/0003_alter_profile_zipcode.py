# Generated by Django 4.0.3 on 2022-03-02 20:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_profile_zipcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='zipcode',
            field=models.CharField(max_length=9, validators=[django.core.validators.RegexValidator(regex='^(^[0-9]{5}(?:-[0-9]{4})?$|^$)')]),
        ),
    ]
