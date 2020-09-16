from django.urls import path, include
from . import views


app_name = 'dhcpd'
urlpatterns = [
    path('', views.DhcpView.as_view(), name='dhcp_lista'),
    path('dhcp', views.DhcpListView.as_view() , name='dhcp_list'),
    #path('api/', include('appview.api.urls')),
    #path('random/', views.RandomSwitchView.as_view(), name='random_switch'),

] 
