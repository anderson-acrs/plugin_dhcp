# Generated by Django 3.1 on 2020-11-12 22:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dhcp', '0055_auto_20201112_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dhcp',
            name='data_criacao',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 12, 22, 25, 38, 681040, tzinfo=utc)),
        ),
    ]