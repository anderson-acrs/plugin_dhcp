from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required, login_required
from .models import Dhcp, Ipfixo
from .forms import DhcpForm, DhcpFilterForm, DhcpCSVForm, IpfixoForm, IpfixoFilterForm, IpfixoCSVForm
from .filter import DhcpFilter, IpfixoFilter
from .tables import DhcpTable, IpfixoTable
from django.views import *
from .utils import get_token, get_user, get_unit, get_server
from netbox.views import generic
from utilities.views import GetReturnURLMixin, ObjectPermissionRequiredMixin

# Create your views here .

#Bloco DHCP
"""Agrupa as Views da classe DHCP"""
class DhcpView(PermissionRequiredMixin, View):     
    permission_required = 'dhcp.dhcp_view'        
    def get(self, request, pk):
        dhcp = get_object_or_404(Dhcp.objects.filter(id_prefixes=pk))
        return render(request, 'dhcp/dhcp_list.html', {
           'dhcp': dhcp
        })
        permissions = {            
            'delete': request.user.has_perm('dhcp.bulk_delete_dhcp'),
        }
        
class DhcpListView (PermissionRequiredMixin, generic.ObjectListView ):
    permission_required = 'dhcp.dhcp_view'
    queryset = Dhcp.objects.all()
    filterset = DhcpFilter
    filterset_form = DhcpFilterForm
    table = DhcpTable
    action_buttons = ('export')
    template_name = 'dhcp/dhcp_list.html'

class DhcpCreateView(PermissionRequiredMixin, generic.ObjectEditView):
    permission_required = 'dhcp.add_dhcp'
    model = Dhcp
    queryset = Dhcp.objects.all()
    model_form = DhcpForm
    
class DhcpEditView(DhcpCreateView):
    permission_required = 'dhcp.change_dhcp'
    
    
class DhcpDeleteView(PermissionRequiredMixin, generic.ObjectDeleteView):
    permission_required = 'dhcp_bulk_delete'
    model = Dhcp
    queryset = Dhcp.objects.all()
    

class DhcpBulkDeleteView(PermissionRequiredMixin, generic.BulkDeleteView):
    permission_required = 'dhcp_bulk_delete'
    queryset = Dhcp.objects.all()
    table = DhcpTable
    default_return_url = 'plugins:dhcp:dhcp_list'

class DhcpBulkImportView(PermissionRequiredMixin, generic.BulkImportView):
    permission_required = 'dhcp.import_dhcp'
    queryset = Dhcp.objects.filter()
    model_form = DhcpCSVForm
    table = DhcpTable
    default_return_url = 'plugins:dhcp:dhcp_list'
    
#Bloco IP Fixo

class IpfixoView( PermissionRequiredMixin, generic.ObjectView): 
    queryset = Ipfixo.objects.prefetch_related(
        'mac_address', 'host', 'prefix' 
    )     
    permission_required = 'dhcp.ipfixo_view'        
    def get(self, request, pk):
        ipfixo = get_object_or_404(self.queryset.restrict, pk=pk)
        return render(request, 'dhcp/ipfixo_list.html', {
           'ipfixo': ipfixo
        })

    def get_extra_context(self, request, instance):
        ipfixo = Ipfixo.object.restrict(request.user, 'view').filter(prefix=instance)
        return {
            'ipfixo': ipfixo,
        }
        
        permissions = {            
            'delete': request.user.has_perm('ipfixo.delete_ipfixo'),
        }
#Pagina de View OK
class IpfixoListView ( PermissionRequiredMixin, generic.ObjectListView): #
    permission_required = 'dhcp.view_ipfixo'
    queryset = Ipfixo.objects.prefetch_related(
        'mac_address', 'host', 'prefix'  
    )   
    filterset = IpfixoFilter
    filterset_form = IpfixoFilterForm
    table = IpfixoTable
    template_name = 'dhcp/ipfixo_list.html'
    action_buttons = ( 'add','import','export')

#Pagina de View OK
class IpfixoCreateView(PermissionRequiredMixin, generic.ObjectEditView):  
    permission_required = 'dhcp.add_ipfixo'
    model = Ipfixo
    queryset = Ipfixo.objects.all()   
    model_form = IpfixoForm
    action_buttons = ( 'export')
    template_name = 'dhcp/ipfixo_add.html'

#Pagina de View OK
class IpfixoEditView(IpfixoCreateView):
    action_buttons = ( 'import','export')
    default_return_url = 'plugins:dhcp:ipfixo_list'
     
class IpfixoDeleteView(PermissionRequiredMixin, generic.ObjectDeleteView):
    permission_required = 'dhcp.delete_ipfixo'
    queryset = Ipfixo.objects.all()
    default_return_url = 'plugins:dhcp:ipfixo_list'

class IpfixoBulkDeleteView( PermissionRequiredMixin, generic.BulkDeleteView):  #
    permission_required = 'ipfixo.delete_ipfixo'
    queryset = Ipfixo.objects.all()
    table = IpfixoTable
    default_return_url = 'plugins:dhcp:ipfixo_list'

class IpfixoBulkImportView(PermissionRequiredMixin, generic.BulkImportView):
    permission_required = 'ipfixo.import_ipfixo'
    queryset = Ipfixo.objects.filter()
    model_form = IpfixoCSVForm 
    table = IpfixoTable 
    default_return_url = 'plugins:dhcp:ipfixo_list'

