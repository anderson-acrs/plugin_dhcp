# Generated by Django 3.1 on 2020-11-10 14:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dhcp', '0010_auto_20201110_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dhcp',
            name='data_criacao',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 10, 14, 50, 14, 676997, tzinfo=utc)),
        ),
    ]
