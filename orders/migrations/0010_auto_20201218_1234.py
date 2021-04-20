# Generated by Django 2.2.17 on 2020-12-18 09:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_auto_20201216_1826'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('tel', models.CharField(max_length=10)),
                ('address', models.TextField()),
                ('email', models.CharField(max_length=30)),
                ('role', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_date',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 12, 18, 9, 34, 56, 173084, tzinfo=utc)),
        ),
    ]