from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth.mixins import PermissionRequiredMixin
from .forms import DhcpForm
from .models import Dhcp
from django.views import View
from  utilities.views import ObjectListView

# Create your views here.
class DhcpView(PermissionRequiredMixin, View): 
    permission_required = 'dhcpd.dhcp_view'
    def get(self,request):
        dhcp = Dhcp.objects.all()
        return render(request, 'dhcpd/dhcp_list.html',{
            'dhcp_list': dhcp,
        })
        
class DhcpListView (ObjectListView):
    permission_required = 'dhcpd.view_dhcplistview'
    queryset = Dhcp.objects.all()
    template_name = 'dhcpd/dhcp_list.html'