from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required, login_required
from .models import Dhcp, Ipfixo
from .forms import DhcpForm, DhcpFilterForm, DhcpCSVForm, IpfixoForm, IpfixoFilterForm, IpfixoCSVForm
from .filter import DhcpFilter, IpfixoFilter
from .tables import DhcpTable, IpfixoTable
from django.views import View
#from django.views.generic.base import TemplateView
from .utils import get_token, get_user, get_unit, get_server
#from  utilities.views import ObjectListView, ObjectEditView, ObjectDeleteView, BulkDeleteView, ComponentCreateView, ObjectView, BulkImportView
from netbox.views import generic
from utilities.views import GetReturnURLMixin, ObjectPermissionRequiredMixin

# Create your views here .

#Bloco DHCP
"""Agrupa as Views da classe DHCP"""
class DhcpView(PermissionRequiredMixin, View):     
    permission_required = 'dhcp.dhcp_view'        
    def get(self, request, pk):
        dhcp = get_object_or_404(Dhcp.objects.filter(id_prefixes=pk))
        return render(request, 'dhcp/dhcp.html', {
           'dhcp': dhcp
        })
        
class DhcpListView (PermissionRequiredMixin, generic.ObjectListView ):
    permission_required = 'dhcp.dhcp_view'
    queryset = Dhcp.objects.all()
    filterset = DhcpFilter
    filterset_form = DhcpFilterForm
    table = DhcpTable
    action_buttons = ('export')
    #template_name = 'dhcp/dhcp_list.html'

class DhcpCreateView(PermissionRequiredMixin, generic.ObjectEditView):
    permission_required = 'dhcp.add_dhcp'
    model = Dhcp
    queryset = Dhcp.objects.all()
    model_form = DhcpForm
    #template_name = 'dhcp/dhcp_add.html'
    #default_return_url = 'plugins:dhcp:dhcp_list'

class DhcpEditView(DhcpCreateView):
    permission_required = 'dhcp.change_dhcp'
    
    

class DhcpDeleteView(PermissionRequiredMixin, generic.ObjectDeleteView):
    permission_required = 'dhcp.delete_dhcp'
    model = Dhcp
    queryset = Dhcp.objects.all()
    #default_return_url = 'plugins:dhcp:dhcp_list'

class DhcpBulkDeleteView(PermissionRequiredMixin, generic.BulkDeleteView):
    permission_required = 'dhcp.delete_dhcp'
    queryset = Dhcp.objects.filter()
    filterset = DhcpFilter
    table = DhcpTable
    model_form = DhcpForm
    #default_return_url = 'plugins:dhcp:dhcp_list'

class DhcpBulkImportView(PermissionRequiredMixin, generic.BulkImportView):
    permission_required = 'dhcp.import_dhcp'
    queryset = Dhcp.objects.filter()
    model_form = DhcpCSVForm
    table = DhcpTable
    default_return_url = 'plugins:dhcp:dhcp_list'
    
#Bloco IP Fixo
#class IpfixoView(PermissionRequiredMixin, View):  
class IpfixoView(generic.ObjectView):     
    permission_required = 'dhcp.ipfixo_view'        
    def get(self, request, pk):
        ipfixo = get_object_or_404(Ipfixo.objects.filter(id_ipfixo=pk))
        return render(request, 'dhcp/ipfixo_list.html', {
           'ipfixo': ipfixo
        })
#Pagina de View OK
class IpfixoListView ( PermissionRequiredMixin, generic.ObjectListView): #
    permission_required = 'dhcp.view_ipfixo'
    #queryset = Ipfixo.objects.all() 
    queryset = Ipfixo.objects.prefetch_related(
        'mac_address', 'host', 'prefix'  #, 'tenant', 'role', 'prefixes'
    )   
    filterset = IpfixoFilter
    filterset_form = IpfixoFilterForm
    table = IpfixoTable
    template_name = 'dhcp/ipfixo_list.html'
    #action_buttons = ('add', 'import', 'export')
    action_buttons = ( 'export')


#Pagina de View OK
class IpfixoCreateView(PermissionRequiredMixin, generic.ObjectEditView):  
    permission_required = 'dhcp.add_ipfixo'
    model = Ipfixo
    queryset = Ipfixo.objects.all()   
    model_form = IpfixoForm
    action_buttons = ( 'export')
    template_name = 'dhcp/ipfixo_add.html'
    #default_return_url = 'plugins:dhcp:ipfixo_list'
#Pagina de View OK
class IpfixoEditView(IpfixoCreateView):
    #permission_required = 'ipfixo.change_ipfixo'
    action_buttons = ( 'import','export')
    
    
class IpfixoDeleteView(generic.ObjectDeleteView):
    #permission_required = 'dhcp.delete_ipfixo'
    queryset = Ipfixo.objects.all()
    model = Ipfixo
    #default_return_url = 'plugins:dhcp:ipfixo_list'

class IpfixoBulkDeleteView(generic.BulkDeleteView):
    #permission_required = 'dhcp.delete_ipfixo'
    queryset = Ipfixo.objects.filter()
    filterset = IpfixoFilter
    table = IpfixoTable
    model_form = IpfixoForm
    template_name = 'dhcp/ipfixo_list.html'
    #default_return_url = 'plugins:dhcp:ipfixo_list'
    #Final ipfixo

class IpfixoBulkImportView(PermissionRequiredMixin, generic.BulkImportView):
    permission_required = 'ipfixo.import_ipfixo'
    queryset = Ipfixo.objects.filter()
    model_form = IpfixoCSVForm 
    table = IpfixoTable 
    default_return_url = 'plugins:dhcp:ipfixo_list'

