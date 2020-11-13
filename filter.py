import django_filters
from django.db.models import Q
from utilities.filters import NameSlugSearchFilterSet, BaseFilterSet, MultiValueCharFilter, TagFilter
from .models import Dhcp, Ipfixo


class DhcpFilter(NameSlugSearchFilterSet):
    q = django_filters.CharFilter(
        method="search",
        label="Search",
    )

    class Meta:
        model = Dhcp
        fields = [
            'prefix',           
            ]
    def search(self, queryset, prefix, value):
        if not value.strip():
            return queryset

        qs_filter = (
            #Q(id_prefixes__icontains=value)
            Q(prefix__icontains=value)            
        )
        return queryset.filter(qs_filter)


#IPFixoFilter
class IpfixoFilter(NameSlugSearchFilterSet):
    q = django_filters.CharFilter(
        method="search",
        label="Search",
    )
    #Modifiquei aqui 01 modelo ipaddressfilterset, linha 287
    address = MultiValueCharFilter(
        method='filter_address',
        label='Address',
    )
    prefix = django_filters.CharFilter(
        method='prefix',
        label='Prefix',
    )
    tag = TagFilter()
    class Meta:
        model = Ipfixo       
        fields = [
            'host',
            'mac_address' ,          
            ]
    def search(self, queryset, name, value): #acrescentei o name e tirei o host
        if not value.strip():
            return queryset

        qs_filter = (
            Q(host__icontains=value)
          | Q(mac_address__icontains=value)                    
        )
        return queryset.filter(qs_filter)
        #acrescentei da linha 57-61
        def filter_address(self, queryset, name, value):
            try:
                return queryset.filter(address__net_in=value)
            except ValidationError:
                return queryset.none()