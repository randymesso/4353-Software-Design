# Generated by Django 4.0.2 on 2022-05-06 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0012_delete_pricing_module'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientinformation',
            name='state',
            field=models.CharField(choices=[('AL', 'AL'), ('AK', 'AK'), ('AZ', 'AZ'), ('AR', 'AR'), ('CA', 'CA'), ('CO', 'CO'), ('CT', 'CT'), ('DE', 'DE'), ('DC', 'DC'), ('FL', 'FL'), ('GA', 'GA'), ('HI', 'HI'), ('ID', 'ID'), ('IL', 'IL'), ('IN', 'IN'), ('IA', 'IA'), ('KY', 'KY'), ('LA', 'LA'), ('ME', 'ME'), ('MD', 'MD'), ('MA', 'MA'), ('MI', 'MI'), ('MN', 'MN'), ('MS', 'MS'), ('MO', 'MO'), ('MT', 'MT'), ('NE', 'NE'), ('NV', 'NV'), ('NH', 'NH'), ('NJ', 'NJ'), ('NM', 'NM'), ('NY', 'NY'), ('ND', 'ND'), ('OH', 'OH'), ('OK', 'OK'), ('OR', 'OR'), ('PA', 'PA'), ('RI', 'RI'), ('SD', 'SD'), ('TN', 'TN'), ('TX', 'TX'), ('UT', 'UT'), ('VT', 'VT'), ('VA', 'VA'), ('WA', 'WA'), ('WV', 'WV'), ('WI', 'WI'), ('WY', 'WY')], max_length=2),
        ),
    ]
