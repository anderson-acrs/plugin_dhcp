from django.contrib import admin
from .models import Dhcp, Ipfixo, Responsavel, Servico

# Register your models here.


@admin.register(Dhcp)
class DhcpAdmin(admin.ModelAdmin):
   list_display = ('prefixes', 'netmask', 'id_domain', 'gateway', 'option', 'tipo', 'ip_inicial', 'ip_final', 'data_criacao')


@admin.register(Responsavel)
class ResponsavelAdmin(admin.ModelAdmin):
    list_display = ('nome', 'contato')

@admin.register(Ipfixo)
class IpfixoAdmin(admin.ModelAdmin):
    list_display = ('id_prefixes', 'mac_address', 'ip_host', 'host', 'defaultleasetime','maxleasetime' )
    
@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'protocol', 'port_number','ip_address', 'description')
