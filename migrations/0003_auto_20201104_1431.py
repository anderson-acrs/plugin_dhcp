# Generated by Django 3.1 on 2020-11-04 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dhcp', '0002_auto_20201104_1423'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dhcp',
            old_name='id_servico',
            new_name='id_service',
        ),
        migrations.RenameField(
            model_name='dhcp',
            old_name='opcao',
            new_name='option',
        ),
    ]
