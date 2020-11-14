# Generated by Django 3.1 on 2020-11-13 21:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dhcp', '0064_auto_20201113_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dhcp',
            name='data_criacao',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 13, 21, 14, 41, 626406, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ipfixo',
            name='mac_address',
            field=models.CharField(max_length=41, unique=True),
        ),
    ]
