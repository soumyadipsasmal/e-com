# Generated by Django 5.0.2 on 2024-03-15 20:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='Product',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 3, 16, 1, 34, 3, 5131)),
        ),
    ]
