from rest_framework.serializers import ModelSerializer
from dhcp.models import Dhcp, Ipfixo

class DhcpSerializer(ModelSerializer):

    class Meta:
        model = Dhcp
        fields = (
            'prefix',
            'address', 
            'vlan',
           # 'id_domain',
            'gateway',
            'ipaddresses',
            #'dns_name',
            'ip_inicial',
            'ip_final',            
            'option',
            'tipo',
            'data_criacao',            
            'name',
            'defaultleasetime',
            'maxleasetime',
        )

class IpfixoSerializer(ModelSerializer):

    class Meta:
        model = Ipfixo
        fields = (
            'prefix',
            'vlan',
            'mac_address',
            'address',
            'host', 
            )
