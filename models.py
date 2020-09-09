from django.db import models

# Create your models here.

class Servicos(models.Model):
    id_servico = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length = 20)
    protocol = models.CharField(max_length=7)
    port_number = models.IntegerField()
    ip_address = models.GenericIPAddressField()
    description = models.CharField(max_length=100)


class Dhcp(models.Model):
    id_prefixes = models.IntegerField(primary_key=True)
    prefixes = models.GenericIPAddressField()
    netmask = models.GenericIPAddressField()
    id_domain = models.IntegerField()
    gateway = models.GenericIPAddressField()
    opcao = models.IntegerField()
    tipo = models.CharField(max_length=4)
    ip_inicial = models.GenericIPAddressField()
    ip_final = models.GenericIPAddressField()
    data_criacao = models.DateTimeField('date published')
    id_servico = models.ForeignKey(
        to='dhcpd.Dhcp',
        on_delete=models.PROTECT,
        related_name='servico',
    ) 
    id_resp = models.ForeignKey(
        to='dhcpd.Dhcp',
        on_delete=models.PROTECT,
        related_name='responsavel',
    )

class Ipfixo(models.Model):
    id_ipfixo = models.IntegerField(primary_key=True)
    id_prefixes = models.ForeignKey(Dhcp, on_delete=models.CASCADE)
    mac = models.CharField(max_length=16)
    ip_host = models.GenericIPAddressField()
    host = models.CharField(max_length=20)
    defaultleasetime = models.IntegerField()
    maxleasetime = models.IntegerField()

class Responsavel(models.Model):
    id_resp = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=20)
    contato = models.CharField(max_length=20)