from django.db import models
from django.urls import reverse
from .choices import DhcpChoices, DhcpOpcaoChoices
#from datetime import date, datetime
from django.utils import timezone

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
    prefixes = models.GenericIPAddressField()
    netmask = models.GenericIPAddressField()
    id_domain = models.IntegerField()
    gateway = models.GenericIPAddressField()
    option = models.CharField(max_length=2, choices=DhcpOpcaoChoices, default=DhcpOpcaoChoices.TIPO_43,)
    tipo = models.CharField(max_length=9, choices=DhcpChoices, default=DhcpChoices.TIPO_IPV4,)
    ip_inicial = models.GenericIPAddressField()
    ip_final = models.GenericIPAddressField()
    #data_criacao = models.DateTimeField('date published')
    data_criacao = models.DateTimeField(default=timezone.now())
    #data_criacao = models.DateTimeField(django.utils.datetime.now())
    # device = models.ForeignKey(
    #     to='dcim.Device',
    #     on_delete=models.CASCADE,
    #     related_name='services',
    #     verbose_name='device',
    #     null=True,
    #     blank=True,
        
    # )
    id_service = models.ForeignKey(Servico, on_delete=models.PROTECT)
    id_resp = models.ForeignKey('Responsavel', on_delete=models.PROTECT)
    defaultleasetime = models.IntegerField()
    maxleasetime = models.IntegerField()
       
    def __str__(self):
        return  self.prefixes 

    # def get_absolute_url(self):
    #     return reverse('ipam:service', args=[self.pk])

    def get_absolute_url(self):
        return reverse('plugins:dhcp:dhcp_list')
        #return reverse('dhcpd:dhcp', args=[self.pk], kwargs={"pk": self.pk})


class Ipfixo(models.Model):
    id_ipfixo = models.AutoField(primary_key=True)
    id_prefixes = models.ForeignKey(Dhcp, on_delete=models.PROTECT)
    mac_address = models.CharField(max_length=17)
    ip_host = models.GenericIPAddressField()
    host = models.CharField(max_length=20)
    
    

    def __str__(self):
        return  self.host

    def get_absolute_url(self):
        return reverse('plugins:dhcp:ipfixo_list')
class Responsavel(models.Model):
    id_resp = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=20)
    contato = models.CharField(max_length=20)