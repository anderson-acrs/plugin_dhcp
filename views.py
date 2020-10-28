from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required, login_required
from .models import Dhcp, Ipfixo, Responsavel
from .forms import DhcpForm, DhcpFilterForm, IpfixoForm, IpfixoFilterForm, ResponsavelForm
from .filter import DhcpFilter
from .tables import DhcpTable, IpfixoTable, ResponsavelTable
from django.views import View
from  utilities.views import ObjectListView, ObjectEditView, ObjectDeleteView, BulkDeleteView, ComponentCreateView

# Create your views here.

#Bloco DHCP
"""Agrupa as Views da classe DHCP"""
class DhcpView(PermissionRequiredMixin, View):     
    permission_required = 'dhcp.dhcp_view'        
    def get(self, request, pk):
        dhcp = get_object_or_404(Dhcp.objects.filter(id_prefixes=pk))
        return render(request, 'dhcpd/dhcp.html', {
           'dhcp': dhcp
        })
        
class DhcpListView (PermissionRequiredMixin, ObjectListView):
    permission_required = 'dhcp.dhcp_view'
    queryset = Dhcp.objects.all()
    filterset = DhcpFilter
    filterset_form = DhcpFilterForm
    table = DhcpTable
    template_name = 'dhcpd/dhcp_list.html'

class DhcpCreateView(PermissionRequiredMixin, ObjectEditView):
    permission_required = 'dhcp.add_dhcp'
    model = Dhcp
    queryset = Dhcp.objects.all()
    model_form = DhcpForm
    template_name = 'dhcpd/dhcp_add.html'
    default_return_url = 'dhcpd:dhcp_list'

class DhcpEditView(DhcpCreateView):
    permission_required = 'dhcp.change_dhcp'
    
    

class DhcpDeleteView(PermissionRequiredMixin, ObjectDeleteView):
    permission_required = 'dhcp.delete_dhcp'
    model = Dhcp
    default_return_url = 'dhcpd:dhcp_list'

class DhcpBulkDeleteView(PermissionRequiredMixin, BulkDeleteView):
    permission_required = 'dhcp.delete_dhcp'
    queryset = Dhcp.objects.filter()
    table = DhcpTable
    default_return_url = 'dhcp:dhcp_list'

#Bloco IP Fixo
class IpfixoListView (PermissionRequiredMixin, ObjectListView):
    permission_required = 'dhcp.view_ipfixo'
    queryset = Ipfixo.objects.all()    
    filterset_form = IpfixoFilterForm
    table = IpfixoTable
    template_name = 'dhcpd/dhcp_list.html'


#View Responsavel
class ResponsavelView(PermissionRequiredMixin, View):
    permission_required = 'dhcp.dhcp_view'
    def get(self, request, pk):
        responsavel = get_object_or_404(Responsavel, pk=pk)
        resonsavel_table = tables.ResponsavelTable(
            ResponsavelTable.objects.filter(responsavel=responsavel),
            orderable = false
        )
        return render(request, 'dhcpd/responsavel.html', {
            'responsavel': responsavel,
        })


class ResponsavelTemplateCreateView(PermissionRequiredMixin, ComponentCreateView):
    permission_required = 'dhcp.add_responsavel'
    model = Responsavel    
    model_form = ResponsavelForm
    template_name = 'dhcpd/responsavel_add.html'
    default_return_url = 'dhcpd:responsavel_add'