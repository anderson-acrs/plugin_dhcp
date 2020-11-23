from rest_framework import routers
from .views import DhcpViewSet, IpfixoViewSet

router = routers.DefaultRouter()
router.register('dhcp', DhcpViewSet)
router.register('ipfixo', IpfixoViewSet)
urlpatterns = router.urls
