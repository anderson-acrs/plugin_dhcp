from django.contrib import admin
from .models import Dhcp, Ipfixo, Servico

# Register your models here.


@admin.register(Dhcp)
class DhcpAdmin(admin.ModelAdmin):
   list_display = ('prefix', 'address', 'id_domain', 'gateway', 'option', 'tipo', 'ip_inicial', 'ip_final', 'data_criacao', 'defaultleasetime','maxleasetime', 'name')


@admin.register(Ipfixo)
class IpfixoAdmin(admin.ModelAdmin):
    list_display = ('mac_address', 'address', 'host' )
    
@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'protocol', 'port_number','ip_address', 'description')
