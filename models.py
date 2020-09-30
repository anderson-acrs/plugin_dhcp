from django.db import models
from .choices import DhcpChoices

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
    opcao = models.IntegerField()
    tipo = models.CharField(max_length=9, choices=DhcpChoices, default=DhcpChoices.TIPO_BOTH,)
    ip_inicial = models.GenericIPAddressField()
    ip_final = models.GenericIPAddressField()
    data_criacao = models.DateTimeField('date published')
    id_servico = models.ForeignKey(Servico, on_delete=models.PROTECT)
    id_resp = models.ForeignKey('Responsavel', on_delete=models.PROTECT)
    
       
    def __str__(self):
        return  {self.id_prefixes} 

    def get_absolute_url(self):
        return reverse('dhcpd:dhcp', args=[self.pk], kwargs={"pk": self.pk})


class Ipfixo(models.Model):
    id_ipfixo = models.AutoField(primary_key=True)
    id_prefixes = models.ForeignKey(Dhcp, on_delete=models.PROTECT)
    mac = models.CharField(max_length=17)
    ip_host = models.GenericIPAddressField()
    host = models.CharField(max_length=20)
    defaultleasetime = models.IntegerField()
    maxleasetime = models.IntegerField()

class Responsavel(models.Model):
    id_resp = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=20)
    contato = models.CharField(max_length=20)