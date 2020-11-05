from django import forms
from utilities.forms import BootstrapMixin
from .models import Dhcp, DhcpChoices, Ipfixo, Responsavel

BLANK_CHOICE = (("", "---------"),)


class DhcpForm(BootstrapMixin, forms.ModelForm):
    """ classe destinada ao model dhcp"""
    class Meta:
        model = Dhcp
        fields = [
            'prefixes', 
            'netmask',
            'id_domain',
            'gateway',
            'option',
            'tipo',
            'ip_inicial',
            'ip_final',
            'data_criacao',
            'id_service',
            #'device',
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
            'id_prefixes' ,
            'mac_address',
            'ip_host',
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
