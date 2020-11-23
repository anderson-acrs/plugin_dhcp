# Generated by Django 3.1 on 2020-11-20 17:39

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ipam', '0037_ipaddress_assignment'),
        ('dhcp', '0074_auto_20201120_1733'),
    ]

    operations = [
        migrations.AddField(
            model_name='ipfixo',
            name='vrf',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='ipam.vrf'),
        ),
        migrations.AlterField(
            model_name='dhcp',
            name='data_criacao',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 20, 17, 39, 18, 480304, tzinfo=utc)),
        ),
    ]
