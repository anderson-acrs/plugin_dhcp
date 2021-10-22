import netaddr
from ipam.fields import *
from django.db import models
from django.db.models import Q
from ipam.models import Prefix, IPAddress
from dcim.models import Site
from django.urls import reverse
from .choices import DhcpChoices, DhcpOpcaoChoices, DhcpDnsChoices
from django.utils import timezone
from sdns.models import Domain



# Create your models here. #anderson

class Servico(models.Model):
    id_servico = models.AutoField(primary_key=True)
    nome = models.CharField(max_length = 20)
    protocol = models.CharField(max_length=7)
    port_number = models.IntegerField()
    ip_address = models.GenericIPAddressField()
    description = models.CharField(max_length=100)


class Dhcp(models.Model):
    id_prefixes = models.AutoField(primary_key=True)
    prefix = models.OneToOneField(
        to='ipam.Prefix',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
        verbose_name='Prefix'
    )  
    address = models.ForeignKey(
        to='ipam.IPAddress',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,               
        verbose_name='IP de Gerencia',
        help_text='IPv4 or IPv6 address (with mask)',
    )
    gateway = models.GenericIPAddressField(
        help_text= 'IPV4 or IPV6 address (without Mask)'

    )
    vlan = models.ForeignKey( 
        to='ipam.VLAN',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
        verbose_name='VLAN'
    )
    
    
    vrf = models.ForeignKey(
        to='ipam.VRF',
        on_delete=models.PROTECT,
        related_name='+',
        blank=True,
        null=True,
        verbose_name='VRF'
    )  
    id_domain = models.ForeignKey(
        to='sdns.Domain',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,               
        verbose_name='Domain',
        help_text='Identificador de dominio',
    )
    dns_1 = models.CharField(
    max_length=15,
    choices=DhcpDnsChoices,
    default=DhcpDnsChoices.TIPO_DNS1,
    help_text='Primary dns server',
    )
    
    dns_2 = models.CharField(
    max_length=15,
    choices=DhcpDnsChoices,
    default=DhcpDnsChoices.TIPO_DNS2,
    help_text='Second dns server',
    )

    option = models.CharField(max_length=2, choices=DhcpOpcaoChoices, default=DhcpOpcaoChoices.TIPO_43,)
    tipo = models.CharField(max_length=9, choices=DhcpChoices, default=DhcpChoices.TIPO_IPV4,)
    ip_inicial = models.GenericIPAddressField(
        help_text= 'IPV4 or IPV6 address (without Mask)'
    )
    ip_final = models.GenericIPAddressField(
        help_text= 'IPV4 or IPV6 address (without Mask)'
    )    
    ipaddresses = models.ForeignKey(  
        to='ipam.IPAddress',
        on_delete=models.PROTECT,
        related_name='+',                    
        verbose_name='DHCP Server'
    )
    defaultleasetime = models.IntegerField(default=86400)
    maxleasetime = models.IntegerField(default=None, null=True) 
          
    data_criacao = models.DateTimeField(default=timezone.now())    
    name = models.ForeignKey( 
        to='dcim.Site',
        on_delete=models.SET_NULL,
        related_name='+',
        null=True,
        verbose_name='Site',
    )

    is_sinfo = models.BooleanField(
        verbose_name='O DHCP é de responsabilidade da SINFO?',
        default=False,
        help_text='Marque essa opcao se o DHCP for gerenciado pela SINFO'
    )

    csv_headers = [
        'prefix', 'address', 'gateway', 'vlan', 'vrf', 'ip_inicial', 'ip_final', 'ipaddress', 'nome']
       
       
    def __str__(self):
        return  str (self.prefix) 
    
    
    def get_absolute_url(self):
        return reverse('plugins:dhcp:dhcp_list')

    def to_csv(self):
        return(
        self.prefix,
        self.address,
        self.gateway,
        self.vlan,
        )

    # def clean(self):
    #     if self.ip_inicial > self.ip_final:
    #         raise ValidationError('The initial IP is higher than the final IP !!')

   
class Ipfixo(models.Model):
    id_ipfixo = models.AutoField(primary_key=True)     
    prefix = models.ForeignKey(  #OneToOneField(
        to='ipam.Prefix',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
        verbose_name='Prefix'
    )
    vrf = models.ForeignKey(
        to='ipam.VRF',
        on_delete=models.PROTECT,
        related_name='+',
        blank=True,
        null=True,
        verbose_name='VRF'
    )  
    vlan = models.ForeignKey( 
        to='ipam.VLAN',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
        verbose_name='VLAN'
    )

    mac_address = models.CharField(max_length=41)    
    host = models.CharField(max_length=20)
    address = models.OneToOneField(
        to='ipam.IPAddress',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,               
        verbose_name='IP Host',
        help_text='IPv4 or IPv6 address (with mask)',
    )
    num_chamado = models.CharField(
        blank=True,
        null=True,
        verbose_name='Numero do Chamado',
        max_length=8,
    ) 
    comments = models.TextField(
        blank=True
    )

    csv_headers = ['prefix','address', 'vlan', 'mac_address',  'host', 'num_chamado']
    
    def __str__(self):
        return  self.host

    def get_absolute_url(self): #1
        return reverse('plugins:dhcp:ipfixo_list')


    #def clean(self):
    #    if self.mac_address:
    #        duplicate_mac_address = self.get_duplicates()
    #        duplicate_prefixes = self.get_duplicates()

    #        if duplicate_mac_address and duplicate_prefixes:
    #            raise ValidationsError({
    #        'mac_address': "Ja existe neste Prefixo", 
    #        duplicate_mac_address.first(),
    #        })

    def to_csv(self):
        return(
            self.prefix,
            self.vlan,
            self.mac_address,
            self.address,
            self.host,
            self.num_chamado
        )


    class Meta:
        constraints = [ models.UniqueConstraint(fields=['prefix', 'mac_address'], name='unique_Mac_address')]

    

