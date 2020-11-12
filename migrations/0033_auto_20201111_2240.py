# Generated by Django 3.1 on 2020-11-11 22:40

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ipam', '0037_ipaddress_assignment'),
        ('dhcp', '0032_auto_20201111_2145'),
    ]

    operations = [
        migrations.AddField(
            model_name='dhcp',
            name='address',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='ipam.ipaddress'),
        ),
        migrations.AlterField(
            model_name='dhcp',
            name='data_criacao',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 11, 22, 40, 29, 308047, tzinfo=utc)),
        ),
    ]
