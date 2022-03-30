import django_tables2 as tables 
from django_tables2.utils import Accessor
from utilities.tables import BaseTable, ToggleColumn, ButtonsColumn, BooleanColumn
from .models import Dhcp, Ipfixo
from ipam.models import Prefix

class DhcpTable(BaseTable):
    """ classe destinada ao model dhcp"""
    pk = ToggleColumn()
    prefix = tables.LinkColumn(  
        verbose_name='Prefix',  
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
            #'id_domain',
            'vlan',
            'gateway',
            'option',
            'tipo',
            'ip_inicial',
            'ip_final',
            'name',
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
            'host',
            'prefix',
            'mac_address',
            'address',
            'vlan',            
        )
