# Generated by Django 3.1 on 2020-11-19 14:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dhcp', '0070_auto_20201117_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dhcp',
            name='data_criacao',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 19, 14, 20, 4, 319389, tzinfo=utc)),
        ),
    ]
