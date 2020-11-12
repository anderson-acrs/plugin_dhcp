# Generated by Django 3.1 on 2020-11-11 19:07

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ipam', '0037_ipaddress_assignment'),
        ('dhcp', '0023_auto_20201111_1259'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dhcp',
            name='id_domain',
        ),
        migrations.AddField(
            model_name='dhcp',
            name='dns_name',
            field=models.OneToOneField(blank=True, max_length=255, null=True, on_delete=django.db.models.deletion.PROTECT, to='ipam.ipaddress'),
        ),
        migrations.AlterField(
            model_name='dhcp',
            name='data_criacao',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 11, 19, 7, 49, 242966, tzinfo=utc)),
        ),
    ]
