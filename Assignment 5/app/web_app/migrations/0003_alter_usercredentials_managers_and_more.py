# Generated by Django 4.0.2 on 2022-04-01 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('web_app', '0002_clientinformation_user'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='usercredentials',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='usercredentials',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AlterField(
            model_name='usercredentials',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AlterField(
            model_name='usercredentials',
            name='username',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]