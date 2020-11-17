import django_filters
import netaddr #Adicionado
from django.db.models import Q
from netaddr.core import AddrFormatError #Adicionado
from utilities.filters import BaseFilterSet, NameSlugSearchFilterSet,  MultiValueCharFilter, TagFilter
from .models import Dhcp, Ipfixo
from ipam.fields import *
from ipam.models import *

#DHCPFIlter
class DhcpFilter(BaseFilterSet, NameSlugSearchFilterSet):
    q = django_filters.CharFilter(
        method="search",
        label="Search",    
    )
    vid = django_filters.CharFilter(
        method='filter_vlan',
        label='Vlan',
    )
    prefix = django_filters.CharFilter(
        method='filter_prefix',
        label='Prefix',
    ) 
    address = django_filters.CharFilter(
        method='filter_address',
        label='address',
    ) 

    #Modifiquei aqui 01 modelo ipaddressfilterset, linha 287 adicionado linha 14 ate linha 52
    # address = MultiValueCharFilter(
    #     method='filter_address',
    #     label='Address',
    # )
    # prefix = django_filters.CharFilter(
    #     method='filter_prefix',
    #     label='Prefix',
    # )
    #tag = TagFilter()  ##
    class Meta:
        model = Dhcp
        fields = [
            'prefix', 
            'address',
            'tipo'

            ]
    def search(self, queryset, name, value):# value
        if not value.strip():
            return queryset
        qs_filter = ( Q(id_prefixes__icontains=value) |  
                      Q(option__icontains=value)   
                    | Q(tipo__icontains=value)                                
                    )
        #qs_filter = Q(description__icontains=value)
        try:
            prefix = str(netaddr.IPNetwork(value.strip()).cidr)
            qs_filter |= Q(prefix__net_icontains=prefix)
        except (AddrFormatError, ValueError):
            pass
        return queryset.filter(qs_filter)
        #return queryset.filter(qs_filter)


    def filter_vlan(self, queryset, name, value):
            try:
                return queryset.filter(vlan=int(value.strip()))
            except ValidationError:
                return queryset.none()
        
    def filter_prefix(self, queryset, name, value):
        if not value.strip():
            return queryset
        try:
            query = str(netaddr.IPNetwork(value).cidr)
            return queryset.filter(prefix=query)
        except (AddrFormatError, ValueError):
            return queryset.none()
    
    def filter_address(self, queryset, name, value):
        try:
            return queryset.filter(address__net_in=value)
        except ValidationError:
            return queryset.none()

    # def search_contains(self, queryset, name, value):
    #     value = value.strip()
    #     if not value:
    #         return queryset
    #     try:
    #         # Searching by prefix
    #         if '/' in value:
    #             return queryset.filter(prefix__net_contains_or_equals=str(netaddr.IPNetwork(value).cidr))
    #         # Searching by IP address
    #         else:
    #             return queryset.filter(prefix__net_contains=str(netaddr.IPAddress(value)))
    #     except (AddrFormatError, ValueError):
    #         return queryset.none()


#IPFixoFilter
class IpfixoFilter(BaseFilterSet, NameSlugSearchFilterSet):
    q = django_filters.CharFilter(
        method="search",
        label="Search",
    )
    address = MultiValueCharFilter(
        method='filter_address',
        label='Address',
    )
    prefix = django_filters.CharFilter(
        method='filter_prefix',
        label='Prefix',
    ) 
    vid = django_filters.CharFilter(
        method='filter_vlan',
        label='Vlan',
    )
     
    class Meta:
        model = Ipfixo       
        fields = [
            'host',
            'mac_address',          
            'id_ipfixo',
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
        #acrescentei da linha 57-61
    def filter_address(self, queryset, name, value):
        try:
            return queryset.filter(address__net_in=value)
        except ValidationError:
            return queryset.none()

    def filter_vlan(self, queryset, name, value):
            try:
                return queryset.filter(vlan=int(value.strip()))
            except ValidationError:
                return queryset.none()