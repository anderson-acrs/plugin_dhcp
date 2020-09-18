# Generated by Django 3.0.8 on 2020-09-16 21:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dhcpd', '0004_auto_20200909_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dhcp',
            name='id_resp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dhcpd.Responsavel'),
        ),
        migrations.AlterField(
            model_name='dhcp',
            name='id_servico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dhcpd.Servico'),
        ),
        migrations.AlterField(
            model_name='ipfixo',
            name='id_prefixes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dhcpd.Dhcp'),
        ),
    ]