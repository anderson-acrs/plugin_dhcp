import django_tables2 as tables 
from django_tables2.utils import Accessor
from utilities.tables import BaseTable, ToggleColumn, ButtonsColumn, BooleanColumn,TagColumn, ToggleColumn
from .models import Dhcp, Ipfixo, Responsavel

class DhcpTable(BaseTable):
    """ classe destinada ao model dhcp"""
    pk = ToggleColumn()
    prefixes = tables.LinkColumn(    
        viewname='plugins:dhcp:dhcp_edit',
        args=[Accessor('pk')]
    )
    class Meta(BaseTable.Meta):
        model = Dhcp
        fields = (
            'pk',
            'id_prefixes',
            'ipaddresses',
            'prefix',
            'id_domain',
            'gateway',
            'option',
            'tipo',
            'ip_inicial',
            'ip_final',
            'data_criacao',
            'defaultleasetime',
            'maxleasetime',
        )
        default_columns = ('pk','prefixes', 'ipaddresses')


class IpfixoTable(BaseTable):
    """ classe destinada ao model ipfixo"""
    pk = ToggleColumn()
    host = tables.LinkColumn(
        viewname = 'plugins:dhcp:ipfixo_edit',
        args = [Accessor('pk')]
    )


    class Meta(BaseTable.Meta):
        model = Ipfixo
        fields = (
            'pk',
            'prefix',
            'mac_address',
            'ip_host',
            'host',
            
        )
class ResponsavelTable(BaseTable):
    """ classe destinada ao model Responsavel"""
    pk = ToggleColumn()
    nome = tables.LinkColumn(
        #viewname='dhcpd:dhcp_edit',
        #args=[Accessor('pk')]
        order_by=('nome',)
    )
    class Meta(BaseTable.Meta):
        model = Responsavel
        fields = (
            'pk',
            'nome',
            'contato',
        )
