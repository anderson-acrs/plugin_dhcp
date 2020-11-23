from django import forms
from utilities.forms import BootstrapMixin, DynamicModelChoiceField, CSVChoiceField
from .models import Dhcp, DhcpChoices, Ipfixo
from extras.forms import CustomFieldModelCSVForm
from ipam.models import *
#from utilities.forms import DynamicModelChoiceField



BLANK_CHOICE = (("", "---------"),)


class DhcpForm(BootstrapMixin, forms.ModelForm):
    """ classe destinada ao model dhcp"""
   
    vlan = DynamicModelChoiceField(
        queryset=VLAN.objects.all(),
        required=False,
        label='VLAN',
        display_field='display_name',
        query_params={
            'site_id': '$site',
            'group_id': '$vlan_group',
        }
    )
    class Meta:
        model = Dhcp
        fields = [
            'prefix',
            'address', 
            'vlan',
            'id_domain',
            'gateway',
            'ipaddresses',
            #'dns_name',
            'ip_inicial',
            'ip_final',            
            'option',
            'tipo',
            'data_criacao',            
            'name', #local
            'defaultleasetime',
            'maxleasetime',
            #'id_resp',   
        ]

class DhcpFilterForm(BootstrapMixin, forms.ModelForm):
    """ classe destinada ao model dhcp"""
    q = forms.CharField(
        required=False,
        label='Search',
    )
    
    class Meta:
        model = Dhcp
        fields = [
            'q',
            'prefix',
            'vlan',           
        ]

class DhcpCSVForm(CustomFieldModelCSVForm):
    model = Dhcp
    fields = Dhcp.csv_headers
    class Meta:
        model = Dhcp
        fields = [
            'prefix',
            'address', 
            'vlan',
            #'id_domain',
            'gateway',
            'ipaddresses',
            #'dns_name',
            'ip_inicial',
            'ip_final',            
            #'option',
            #'tipo',
            #'data_criacao',            
            #'name', #local
            #'defaultleasetime',
            #'maxleasetime',
            #'id_resp',   
        ]


class IpfixoForm(BootstrapMixin, forms.ModelForm):
    """ classe destinada ao model Ipfixo"""
    class Meta:
        model = Ipfixo
        fields = [         
            'prefix',
            'vlan',
            'mac_address',
            'address',
            'host',                        
            'num_chamado',
            'comments',                       
        ]
class IpfixoFilterForm(BootstrapMixin, forms.ModelForm):
    """ classe destinada ao model Ipfixo"""
    #model = Ipfixo
    #field_order = ['q','host','mac_address']
    q = forms.CharField(
        required=False,
        label="Buscador",
    )
    
    class Meta:
        model = Ipfixo
        fields = [
            'q',
            'prefix',
            'vlan',              
       ]
