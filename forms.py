from django import forms
from utilities.forms import BootstrapMixin, DynamicModelChoiceField
from .models import Dhcp, DhcpChoices, Ipfixo, Responsavel 
from ipam.models import Prefix, VLAN, IPAddress



BLANK_CHOICE = (("", "---------"),)


class DhcpForm(BootstrapMixin, forms.ModelForm):
    """ classe destinada ao model dhcp"""

    # ipaddresses = DynamicModelChoiceField(
    #     queryset=IPAddress.objects.all(),
    #     required=False,
    #     label='IP Server',
    #     display_field='display_name',
    #     # query_params={
    #     #     'ipadress':'$address',
    #     # }
    # )
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
            'address', 
            'prefix',
            'vlan',
            'id_domain',
            #'dns_name',
            'gateway',
            'option',
            'tipo',
            'ip_inicial',
            'ip_final',
            'data_criacao',
            'ipaddresses',
            'local',
            'defaultleasetime',
            'maxleasetime',
            'id_resp',   

        ]

class DhcpFilterForm(BootstrapMixin, forms.ModelForm):
    """ classe destinada ao model dhcp"""
    q = forms.CharField(
    required=False,
    label="Buscador",
    )
    # tipo = forms.ChoiceField(
    #     choices=BLANK_CHOICE + DhcpChoices.CHOICES,
    #     required=False
    # )
    class Meta:
        model = Dhcp
        fields = [
            'q',
            # 'prefixes',
            # 'gateway',           
        ]


class IpfixoForm(BootstrapMixin, forms.ModelForm):
    """ classe destinada ao model Ipfixo"""
    class Meta:
        model = Ipfixo
        fields = [
            #'id_prefixes' ,
            'prefix',
            'mac_address',
            #'ipaddress',
            'address',
            #'ip_host',
            'host',
                       
        ]
class IpfixoFilterForm(BootstrapMixin, forms.ModelForm):
    """ classe destinada ao model Ipfixo"""
    q = forms.CharField(
    required=False,
    label="Buscador",
    )
    class Meta:
        model = Ipfixo
        fields = [
            'q',
            'host',
            'mac_address',
                    
        ]
class ResponsavelForm(BootstrapMixin, forms.ModelForm):
    """ classe destinada ao model Responsavel"""
    class Meta:
        model = Responsavel
        fields = [
            'id_resp',
            'nome',            
            'contato',
        ]
