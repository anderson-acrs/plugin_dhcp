# Generated by Django 3.1 on 2020-11-13 21:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dhcp', '0063_auto_20201113_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dhcp',
            name='data_criacao',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 13, 21, 1, 26, 119404, tzinfo=utc)),
        ),
    ]