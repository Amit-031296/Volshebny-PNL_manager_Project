# Generated by Django 2.2 on 2019-09-19 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0013_auto_20190919_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='service_number_of_passengers',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
