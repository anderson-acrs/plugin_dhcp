import django_filters
import netaddr #Adicionado
from django.db.models import Q
from netaddr.core import AddrFormatError #Adicionado
from utilities.filters import BaseFilterSet, NameSlugSearchFilterSet,  MultiValueCharFilter, TagFilter
from .models import Dhcp, Ipfixo
from ipam.fields import *

#DHCPFIlter
class DhcpFilter(NameSlugSearchFilterSet):
    q = django_filters.CharFilter(
        method="search",
        label="Search",
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
    tag = TagFilter()  ##
    class Meta:
        model = Dhcp
        fields = [
            'prefix', 
            'address',
            'tipo',

            ]
    def search(self, queryset, name, value):# value
        if not value.strip():
            return queryset
        qs_filter = ( Q(local__icontains=value)   
                    | Q(option__icontains=value)   
                    | Q(tipo__icontains=value)                                
                    )
        #qs_filter = Q(description__icontains=value)
        try:
            prefix = str(netaddr.IPNetwork(value.strip()).cidr)
            qs_filter |= Q(prefix__net_contains_or_equals=prefix)
        except (AddrFormatError, ValueError):
            pass
        return queryset.filter(qs_filter)
        #return queryset.filter(qs_filter)
        
    def filter_prefix(self, queryset, name, value):
        if not value.strip():
            return queryset
        try:
            query = str(netaddr.IPNetwork(value).cidr)
            return queryset.filter(prefix=query)
        except (AddrFormatError, ValueError):
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
    class Meta:
        model = Ipfixo       
        fields = [
            'host',
            'mac_address',          
            'address',
            ]
    def search(self, queryset, name, value): #acrescentei o name e tirei o host
        if not value.strip():
            return queryset
        qs_filter = (
            Q(host__icontains=value)
          | Q(mac_address__icontains=value) 
          #| Q(address__icontains=value)                   
        )        
        return queryset.filter(qs_filter)
        #acrescentei da linha 57-61
        def filter_address(self, queryset, name, value):
            try:
                return queryset.filter(address__net_in=value)
            except ValidationError:
                return queryset.none()