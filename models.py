import netaddr
from ipam.fields import *
from django.db import models
from ipam.models import Prefix, IPAddress
from dcim.models import Site
from django.urls import reverse
from .choices import DhcpChoices, DhcpOpcaoChoices
from django.utils import timezone
#from .validators import DNSValidator


# Create your models here.

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
    vlan = models.ForeignKey( #ForeignKey( # OneToOneField(
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
    id_domain = models.IntegerField(null=True) 
    # domain = models.CharField(max_length=30)
    # dns_1 = models.GenericIPAddressField(max_length=30)
    # dns_2 = models.GenericIpaddressField(max_length=30)
    # dns_3 = models.GenericIPAddressField(
    #     max_length=30,
    #     help_text= 'Optional DNS'
    # )   
    
    option = models.CharField(max_length=2, choices=DhcpOpcaoChoices, default=DhcpOpcaoChoices.TIPO_43,)
    tipo = models.CharField(max_length=9, choices=DhcpChoices, default=DhcpChoices.TIPO_IPV4,)
    ip_inicial = models.GenericIPAddressField(
        help_text= 'IPV4 or IPV6 address (without Mask)'
    )
    ip_final = models.GenericIPAddressField(
        help_text= 'IPV4 or IPV6 address (without Mask)'
    )    
    ipaddresses = models.ForeignKey(  #OneToOneField(
        to='ipam.IPAddress',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,               
        verbose_name='DHCP Server'
    )
    id_resp = models.ForeignKey('Responsavel', on_delete=models.PROTECT)
    defaultleasetime = models.IntegerField(default=None)
    maxleasetime = models.IntegerField(default=None)    
    data_criacao = models.DateTimeField(default=timezone.now())    
    name = models.ForeignKey( 
        to='dcim.Site',
        on_delete=models.SET_NULL,
        related_name='+',
        null=True,
        verbose_name='Site',
    )#CharField(max_length=100, null=True, blank=True)
       
       
    #def __str__(self):
     #   return  self.name
    def __str__(self):
        return  str (self.prefix) #or super().__str__()
    
    
    def get_absolute_url(self):
        return reverse('plugins:dhcp:dhcp_list')
        

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

    mac_address = models.CharField(unique=True,max_length=41)    
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
    # comments = CommentField()
    # local_context_data = JSONField(
    #     required=False,
    #     label=''
    # )
   # observation = models.CharField(max_length=255)
    def __str__(self):
        return  self.host
    #def __str__(self):
    #   return str(self.prefix)

    def get_absolute_url(self):
        return reverse('plugins:dhcp:ipfixo_list')
class Responsavel(models.Model):
    id_resp = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=20)
    contato = models.CharField(max_length=20)
    name = models.OneToOneField(
        to='tenancy.Tenant',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
        verbose_name='Tenant',
        max_length=30,
        unique=True
    )
    def __str__(self):
        return  self.nome
