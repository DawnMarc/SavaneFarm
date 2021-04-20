# Generated by Django 2.2.17 on 2021-04-18 10:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0025_auto_20210418_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 18, 10, 23, 0, 594081, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 4, 18, 10, 23, 0, 588102, tzinfo=utc)),
        ),
    ]
