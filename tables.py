import django_tables2 as tables 
from django_tables2.utils import Accessor
from utilities.tables import BaseTable, ToggleColumn
from .models import Dhcp

class DhcpTable(BaseTable):
    pk = ToggleColumn()
    ip_prefixes = tables.LinkColumn(    
        viewname='dhcpd:dhcp',
        args=[Accessor('id_prefixes')]
    )
    class Meta(BaseTable.Meta):
        model = Dhcp
        fields = (
            'pk',
            'id_prefixes',
            'prefixes',
            'id_domain',
            'gateway',
            'opcao',
            'tipo',
            'ip_inicial',
            'ip_final',
            'data_criacao',

        )
