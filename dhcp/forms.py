from django import forms
from utilities.forms import BootstrapMixin, DynamicModelChoiceField, CSVChoiceField, CSVModelForm, CSVModelChoiceField
from .models import Dhcp, Ipfixo
from dhcp.choices import DhcpOpcaoChoices, DhcpChoices, DhcpDnsChoices
from extras.forms import CustomFieldModelCSVForm, CustomFieldModelForm
from ipam.models import *
from dcim.models import Site




BLANK_CHOICE = (("", "---------"),)


class DhcpForm(BootstrapMixin,  CustomFieldModelForm): #forms.ModelForm,
    """ classe destinada ao model dhcp"""
   
    # vlan = DynamicModelChoiceField(
    #     queryset=VLAN.objects.all(),
    #     required=True,
    #     label='VLAN',
    #     display_field='display_name',
    #     query_params={
    #         'site_id': '$site',
    #         'group_id': '$vlan_group',
    #     }
    # )
    class Meta:
        model = Dhcp
        fields = [
            'prefix',
            'address', 
            'vlan',            
            'gateway',
            'ipaddresses',            
            'ip_inicial',
            'ip_final',  
            'tipo',
            'option',
            #'id_domain', 
            'dns_1',
            'dns_2',            
            'data_criacao',            
            'name',
            'is_sinfo',
            'defaultleasetime',
            'maxleasetime',
               
        ]

class DhcpFilterForm(BootstrapMixin, CustomFieldModelForm): #forms.ModelForm,
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

class DhcpCSVForm(CSVModelForm): #CustomFieldModelCSVForm): 121  43
    vlan = CSVModelChoiceField(
        queryset=VLAN.objects.all(),
        required=True,
        to_field_name='name',
        help_text='Required if not assigned to a Prefix',
    )
    
    address = CSVModelChoiceField(
        queryset=IPAddress.objects.all(),
        required=False,
        to_field_name='address',
        help_text='Ip de gerencia',
    )
    
    prefix = CSVModelChoiceField(
        queryset=Prefix.objects.all(),
        to_field_name='prefix',
        required=True,
        help_text='Prefix',
        error_messages={"invalid_choice": "Site not found",},
    )

    option = CSVChoiceField(
        choices=DhcpOpcaoChoices,
        required=False,
        help_text='Opcao DHCP',
        ) #teste 164 #Anderson

    tipo = CSVChoiceField(
        choices=DhcpChoices,
        required=False,
        help_text='Tipo',
        )
    
    ipaddresses = CSVModelChoiceField(
        queryset=IPAddress.objects.all(),
        required=True,
        to_field_name='address',
        help_text='Dhcp Server',
    )
    site = CSVModelChoiceField(
        queryset=Site.objects.all(),
        required=False,
        to_field_name='name',
        help_text='Required if not assigned to a device',
    )   
    defaultleasetime = CSVModelChoiceField(
        queryset=Dhcp.objects.all(),
        required=False,
        help_text='default lease = 86400',
    )
    class Meta:
        #fields = Dhcp.csv_headers
        model = Dhcp
        fields = [
            'vlan', 
            'address',
            'prefix', 
            'option', 
            'tipo', 
            'ipaddresses', 
            'site',
            #'id_domain',
            'gateway',
            'ip_inicial',
            'ip_final',             
            'defaultleasetime',
            'maxleasetime',
            'data_criacao',
        ]


class IpfixoForm(BootstrapMixin, CustomFieldModelForm): #forms.ModelForm, 
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
class IpfixoFilterForm(BootstrapMixin, CustomFieldModelForm): # forms.ModelForm,
    """ classe destinada ao model Ipfixo"""
    
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
class IpfixoCSVForm(CSVModelForm): 
    vlan = CSVModelChoiceField(
        queryset=VLAN.objects.all(),
        required=True,
        to_field_name='name',
        help_text='Required if not assigned to a Prefix',
    )
    
    address = CSVModelChoiceField(
        queryset=IPAddress.objects.all(),
        required=True,
        to_field_name='address',
        help_text='Ip do Host',
    )
    
    prefix = CSVModelChoiceField(
        queryset=Prefix.objects.all(),
        to_field_name='prefix',
        required=True,
        help_text='Prefix',
        error_messages={"invalid_choice": "Site not found",},
    )
    # mac_address = CSVModelChoiceField(
    #     queryset=Ipfixo.objects.all(),
    #     to_field_name='mac_address',
    #     required=True,
    #     help_text='Mac Address',        
    # )
    # host = CSVModelChoiceField(
    #     queryset=Ipfixo.objects.all(),
    #     to_field_name='host',
    #     required=True,
    #     help_text='Host',        
    # )
    # num_chamado = CSVModelChoiceField(
    #     queryset=Ipfixo.objects.all(),
    #     to_field_name='num_chamado',
    #     required=False,
    #     help_text='Numero do Chamado',        
    # )
    class Meta:
        #fields = Ipfixo.csv_headers
        model = Ipfixo
        fields = [
            'prefix',
            'vlan', 
            'address',
            'mac_address',
            'host',
            'num_chamado',
        ]
             
