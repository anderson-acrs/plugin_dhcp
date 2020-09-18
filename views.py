from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Dhcp
from .forms import DhcpForm, DhcpFilterForm
from .filter import DhcpFilter
from .tables import DhcpTable
from django.views import View
from  utilities.views import ObjectListView, ObjectEditView, ObjectDeleteView

# Create your views here.
class DhcpView(PermissionRequiredMixin, View): 
    permission_required = 'dhcpd.dhcp_view'
    def get(self,request):
       # d = get_object_or_404(Dhcp.objects.filter(id_prefixes=pk))
        dhcp = Dhcp.objects.all()
        return render(request, 'dhcpd/dhcp_list.html',{
            'dhcp_list': dhcp,
        })
        
class DhcpListView (ObjectListView):
    permission_required = 'dhcpd.view_dhcp'
    queryset = Dhcp.objects.all()
    filterset = DhcpFilter
    filterset_form = DhcpFilterForm
    table = DhcpTable
    template_name = 'dhcpd/dhcp_list.html'

class DhcpCreateView(ObjectEditView):
    permission_required = 'dhcpd.add_dhcp'
    model = Dhcp
    queryset = Dhcp.objects.all()
    model_form = DhcpForm
    template_name = 'dhcpd/dhcp_edit.html'
    dafault_return_url = 'dhcpd:dhcp_list'

class DhcpEditView(DhcpCreateView):
    permission_required = 'dhcpd.change_dhcp'

class DhcpDeleteView(ObjectDeleteView):
    permission_required = 'dhcpd.delete_dhcp'
    model = Dhcp
    default_return_url = 'dhcpd:dhcp_list'
