from django import forms
from utilities.forms import BootstrapMixin
from .models import Dhcp, DhcpChoices

BLANK_CHOICE = (("", "---------"),)


class DhcpForm(BootstrapMixin, forms.ModelForm):
    class Meta:
        model = Dhcp
        fields = [
            'prefixes', 
            'netmask',
            'id_domain',
            'gateway',
            'opcao',
            'tipo',
            'ip_inicial',
            'ip_final',
            'data_criacao',
            'id_servico',
            'id_resp',            
        ]

class DhcpFilterForm(BootstrapMixin, forms.ModelForm):
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