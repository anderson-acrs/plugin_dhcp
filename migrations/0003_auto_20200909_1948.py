# Generated by Django 3.0.8 on 2020-09-09 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dhcpd', '0002_auto_20200909_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dhcp',
            name='id_prefixes',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='ipfixo',
            name='id_ipfixo',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='responsavel',
            name='id_resp',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='servicos',
            name='id_servico',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
