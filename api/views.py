from rest_framework.viewsets import ModelViewSet
from dhcp.models import Dhcp, Ipfixo
from .serializers import DhcpSerializer, IpfixoSerializer

class DhcpViewSet(ModelViewSet):
    queryset = Dhcp.objects.all()
    serializer_class = DhcpSerializer


class IpfixoViewSet(ModelViewSet):
    queryset = Ipfixo.objects.all()
    serializer_class = IpfixoSerializer
