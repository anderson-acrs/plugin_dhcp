# Generated by Django 3.1 on 2020-11-13 21:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dhcp', '0066_auto_20201113_2119'),
    ]

    operations = [
        migrations.AddField(
            model_name='ipfixo',
            name='comments',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='ipfixo',
            name='num_chamado',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='dhcp',
            name='data_criacao',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 13, 21, 54, 6, 50765, tzinfo=utc)),
        ),
    ]
