import django_tables2 as tables 
from django_tables2.utils import Accessor
from utilities.tables import BaseTable, ToggleColumn, ButtonsColumn, BooleanColumn,TagColumn #,ToggleColumn
from .models import Dhcp, Ipfixo, Responsavel
from ipam.models import Prefix

class DhcpTable(BaseTable):
    """ classe destinada ao model dhcp"""
    pk = ToggleColumn()
    prefix = tables.LinkColumn(    
        viewname='plugins:dhcp:dhcp_edit',
        args=[Accessor('pk')]
    )
    class Meta(BaseTable.Meta):
        model = Dhcp
        fields = (
            'pk',
            'address',
            'id_prefixes',
            'ipaddresses',
            'prefix',
            'id_domain',
            'vlan',
            'gateway',
            'option',
            'tipo',
            'ip_inicial',
            'ip_final',
            'name',# local
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
            'address',
            'vlan',
            #'ipaddress',
            #'ip_host',
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
