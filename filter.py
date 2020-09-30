import django_filters
from django.db.models import Q
from utilities.filters import NameSlugSearchFilterSet
from .models import Dhcp


class DhcpFilter(NameSlugSearchFilterSet):
    q = django_filters.CharFilter(
        method="search",
        label="Search",
    )

    class Meta:
        model = Dhcp
        fields = [
            'prefixes',           
            ]
    def search(self, queryset, prefixes, value):
        if not prefixes.strip():
            return queryset

        qs_filter = (
            #Q(id_prefixes__icontains=value)
            Q(prefixes__icontains=value)            
        )
        return queryset.filter(qs_filter)
