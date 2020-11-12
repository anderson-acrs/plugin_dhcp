from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required, login_required
from .models import Dhcp, Ipfixo, Responsavel
from .forms import DhcpForm, DhcpFilterForm, IpfixoForm, IpfixoFilterForm, ResponsavelForm
from .filter import DhcpFilter
from .tables import DhcpTable, IpfixoTable, ResponsavelTable
from django.views import View
from django.views.generic.base import TemplateView
from .utils import get_token, get_user, get_unit, get_server
from  utilities.views import ObjectListView, ObjectEditView, ObjectDeleteView, BulkDeleteView, ComponentCreateView, ObjectView

# Create your views here.

#Bloco DHCP
"""Agrupa as Views da classe DHCP"""
class DhcpView(PermissionRequiredMixin, View):     
    permission_required = 'dhcp.dhcp_view'        
    def get(self, request, pk):
        dhcp = get_object_or_404(Dhcp.objects.filter(id_prefixes=pk))
        return render(request, 'dhcp/dhcp.html', {
           'dhcp': dhcp
        })
        
class DhcpListView (PermissionRequiredMixin, ObjectListView ):
    permission_required = 'dhcp.dhcp_view'
    queryset = Dhcp.objects.all()
    filterset = DhcpFilter
    filterset_form = DhcpFilterForm
    table = DhcpTable
    template_name = 'dhcp/dhcp_list.html'

class DhcpCreateView(PermissionRequiredMixin, ObjectEditView):
    permission_required = 'dhcp.add_dhcp'
    model = Dhcp
    queryset = Dhcp.objects.all()
    model_form = DhcpForm
    template_name = 'dhcp/dhcp_add.html'
    default_return_url = 'plugins:dhcp:dhcp_list'

class DhcpEditView(DhcpCreateView):
    permission_required = 'dhcp.change_dhcp'
    
    

class DhcpDeleteView(PermissionRequiredMixin, ObjectDeleteView):
    permission_required = 'dhcp.delete_dhcp'
    model = Dhcp
    default_return_url = 'plugins:dhcp:dhcp_list'

class DhcpBulkDeleteView(PermissionRequiredMixin, BulkDeleteView):
    permission_required = 'dhcp.delete_dhcp'
    queryset = Dhcp.objects.filter()
    table = DhcpTable
    default_return_url = 'plugins:dhcp:dhcp_list'

#Bloco IP Fixo
class IpfixoView(PermissionRequiredMixin, View):     
    permission_required = 'dhcp.ipfixo_view'        
    def get(self, request, pk):
        ipfixo = get_object_or_404(Ipfixo.objects.filter(id_prefixes=pk))
        return render(request, 'dhcp/ipfixo.html', {
           'ipfixo': ipfixo
        })

class IpfixoListView (PermissionRequiredMixin, ObjectListView):
    permission_required = 'dhcp.view_ipfixo'
    queryset = Ipfixo.objects.all()    
    filterset_form = IpfixoFilterForm
    table = IpfixoTable
    template_name = 'dhcp/ipfixo_list.html'

class IpfixoCreateView(PermissionRequiredMixin, ObjectEditView):
    permission_required = 'dhcp.add_ipfixo'
    model = Ipfixo
    queryset = Ipfixo.objects.all()
    model_form = IpfixoForm
    template_name = 'dhcp/ipfixo_add.html'
    default_return_url = 'plugins:dhcp:ipfixo_list'

class IpfixoEditView(DhcpCreateView):
    permission_required = 'dhcp.change_ipfixo'
    
    
class IpfixoDeleteView(PermissionRequiredMixin, ObjectDeleteView):
    permission_required = 'dhcp.delete_ipfixo'
    model = Ipfixo
    default_return_url = 'plugins:dhcp:ipfixo_list'

class IpfixoBulkDeleteView(PermissionRequiredMixin, BulkDeleteView):
    permission_required = 'dhcp.delete_ipfixo'
    queryset = Ipfixo.objects.filter()
    table = IpfixoTable
    default_return_url = 'plugins:dhcp:ipfixo_list'
    #Final ipfixo

#View Responsavel
class ResponsavelView(PermissionRequiredMixin, View):
    permission_required = 'dhcp.dhcp_view'
    def get(self, request, pk):
        responsavel = get_object_or_404(Responsavel, pk=pk)
        resonsavel_table = tables.ResponsavelTable(
            ResponsavelTable.objects.filter(responsavel=responsavel),
            orderable = false
        )
        return render(request, 'dhcp/responsavel_add.html', {
            'responsavel': responsavel,
        })


class ResponsavelTemplateCreateView(PermissionRequiredMixin, ComponentCreateView):
    permission_required = 'dhcp.add_responsavel'
    model = Responsavel    
    model_form = ResponsavelForm
    template_name = 'dhcp/responsavel_add.html'
    default_return_url = 'plugins:dhcp:responsavel_add'

class RespView(TemplateView):
    """
    Esta classe mostra o que eu tenho que ver
    """
    template_name ="dhcp/resp.html"
        
    def get_context_data(self, ** kwargs):
       context = super().get_context_data(**kwargs)
       nome = self.kwargs['name']
       resp = get_user(nome)
       unit = get_unit(str(resp[0]['id-unidade']))
       context['login'] = resp[0]['login']
       context['nome'] = resp[0]['nome-pessoa']
       context['mail'] = resp[0]['email']
       context['unidade'] = unit['nome-unidade']
       return context


class ResponsavelObjetcView(ObjectView):
    def get(self, request, pk):

        responsavel = get_object_or_404(self.queryset, pk=pk)
        responsaveis = Responsavel.objects.restrict(request.user, 'view').filter(responsavel=responsavel)
        return render(request, 'dhcp/responsavel.html', {
        'responsavel':responsavel,
    })

