# Generated by Django 3.1 on 2020-11-10 21:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dhcp', '0018_auto_20201110_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dhcp',
            name='data_criacao',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 10, 21, 56, 59, 668679, tzinfo=utc)),
        ),
    ]
