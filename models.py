from django.db import models
from ipam.models import Prefix, IPAddress
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
    vlan = models.OneToOneField( #ForeignKey( # OneToOneField(
        to='ipam.VLAN',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
        verbose_name='VLAN'
    )
    address = models.OneToOneField(
        to='ipam.IPAddress',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,               
        verbose_name='IP de Gerencia',
        help_text='IPv4 or IPv6 address (with mask)',
    )
    prefix = models.OneToOneField(
        to='ipam.Prefix',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
        verbose_name='Prefix'
    )
    #prefixes = models.GenericIPAddressField()
    #netmask = models.GenericIPAddressField()
    id_domain = models.IntegerField(null=True)
    # dns_name = models.OneToOneField(
    #     to='ipam.IPAddress',
    #     on_delete=models.SET_NULL, #PROTECT,#CASCADE, #
    #     max_length=255,
    #     null=True,
    #     #blank=True,
    #     #validators=[DNSValidator],
    #     verbose_name='DNS Name',
    #     help_text='Hostname or FQDN (not case-sensitive)'
    # )


    gateway = models.GenericIPAddressField()
    option = models.CharField(max_length=2, choices=DhcpOpcaoChoices, default=DhcpOpcaoChoices.TIPO_43,)
    tipo = models.CharField(max_length=9, choices=DhcpChoices, default=DhcpChoices.TIPO_IPV4,)
    ip_inicial = models.GenericIPAddressField()
    ip_final = models.GenericIPAddressField()
    #id_service = models.ForeignKey(Servico, on_delete=models.PROTECT)
    ipaddresses = models.ForeignKey(  #OneToOneField(
        to='ipam.IPAddress',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,               
        verbose_name='IP Server'
    )
    id_resp = models.ForeignKey('Responsavel', on_delete=models.PROTECT)
    defaultleasetime = models.IntegerField(default=None)
    maxleasetime = models.IntegerField(default=None)    
    data_criacao = models.DateTimeField(default=timezone.now())    
    local = models.CharField(max_length=100, null=True, blank=True)
    #data_criacao = models.DateTimeField('date published')
    # device = models.ForeignKey(
    #     to='dcim.Device',
    #     on_delete=models.CASCADE,
    #     related_name='services',
    #     verbose_name='device',
    #     null=True,
    #     blank=True,
        
    # )
    
       
    def __str__(self):
        return  self.local
    
    # def save(self, *args, **kwargs):

    #     # Force dns_name to lowercase
    #     self.dns_name = self.dns_name.lower()

    #     super().save(*args, **kwargs)
    #     return self.dns_name

    # def get_absolute_url(self):
    #     return reverse('ipam:service', args=[self.pk])

    def get_absolute_url(self):
        return reverse('plugins:dhcp:dhcp_list')
        #return reverse('dhcpd:dhcp', args=[self.pk], kwargs={"pk": self.pk})


class Ipfixo(models.Model):
    id_ipfixo = models.AutoField(primary_key=True) 
    #id_prefixes = models.ForeignKey(Dhcp, on_delete=models.PROTECT)   
    prefix = models.ForeignKey(  #OneToOneField(
        to='ipam.Prefix',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
        verbose_name='Prefix'
    )

    mac_address = models.CharField(unique=True,max_length=17)
    #ip_host = models.GenericIPAddressField()
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
    
    
    

    def __str__(self):
        return  self.host

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

    # def get_absolute_url(self):
    #     return reverse('plugins:dhcp:ipfixo_list')