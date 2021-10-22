import django_filters
import netaddr #Adicionado
from django.db.models import Q
from netaddr.core import AddrFormatError #Adicionado
#from utilities.filters import BaseFilterSet, NameSlugSearchFilterSet,  MultiValueCharFilter
from .models import Dhcp, Ipfixo
from ipam.fields import *
from ipam.models import *
from netbox.filtersets import *

#DHCPFIlter
class DhcpFilter( PrimaryModelFilterSet):
    q = django_filters.CharFilter(
        method="search",
        label="Search",    
    )
    vlan = django_filters.CharFilter(
        method='filter_vlan',
        label='Vlan',
    )
    prefix = django_filters.CharFilter(
         method='filter_prefix',
         label='Prefix',
    ) 
    
    class Meta:
        model = Dhcp
        fields = [
            'q',
            'prefix',
            'vlan',
                        
            ]
    def search(self, queryset, name, value):# value
        if not value.strip():
            return queryset
        qs_filter = ( Q(id_prefixes__icontains=value) |                       
                      Q(option__icontains=value)   
                    | Q(tipo__icontains=value) 
                    #| Q(address__icontains=value)    #istartswith                           
        )
        return queryset.filter(qs_filter)
        
    def filter_vlan(self, queryset, name, value):
            try:
                return queryset.filter(vlan=int(value))                
            except ValidationError:
                return queryset.none()
        
    def filter_prefix(self, queryset, name, value):                   
        try:                
            query = str(netaddr.IPNetwork(value).cidr)
            return queryset.filter(prefix=int(value)) 
        except ValidationError:
            return queryset.none()
      
    def search_contains(self, queryset, name, value):
        value = value.strip()
        if not value:
            return queryset
        try:
            #Searching by prefix
            if '/' in value:
                return queryset.filter(prefix__net_contains_or_equals=str(netaddr.IPNetwork(value).cidr))
            #Searching by IP address
            else:
                return queryset.filter(prefix__net_contains=str(netaddr.IPAddress(value)))
        except (AddrFormatError, ValueError):
                return queryset.none()


#IPFixoFilter
class IpfixoFilter( PrimaryModelFilterSet):
    q = django_filters.CharFilter(
        method="search",
        label="Search",    
    )
    vlan = django_filters.CharFilter(
        method='filter_vlan',
        label='Vlan',
    )
    prefix = django_filters.CharFilter(
         method='filter_prefix',
         label='Prefix',
    ) 
     
    class Meta:
        model = Ipfixo       
        fields = [
            'q',
            'prefix',          
            'vlan',
            ]
    def search(self, queryset, name, value): #acrescentei o name e tirei o host
        if not value.strip():
            return queryset
        qs_filter = (
            Q(host__icontains=value)
          | Q(mac_address__icontains=value) 
          #| Q(address__icontains=value)                   
        )  
        try:#
            qs_filter |= Q(id_ipfixo=int(value.strip()))
        except ValueError:
            pass      
        return queryset.filter(qs_filter)
        

    def filter_vlan(self, queryset, name, value):
            try:
                return queryset.filter(vlan=int(value))
            except ValidationError:
                return queryset.none()
    def filter_prefix(self, queryset, name, value):                   
        try:                
            query = str(netaddr.IPNetwork(value).cidr)
            return queryset.filter(prefix=int(value)) 
        except ValidationError:
            return queryset.none()