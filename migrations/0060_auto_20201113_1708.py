# Generated by Django 3.1 on 2020-11-13 17:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dhcp', '0059_auto_20201112_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dhcp',
            name='data_criacao',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 13, 17, 8, 37, 483618, tzinfo=utc)),
        ),
    ]