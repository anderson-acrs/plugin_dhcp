from django.urls import path, include, re_path
from . import views
from extras.views import *

""" comentario """
#app_name = 'dhcp'
urlpatterns = [
    #DHCP
    path('', views.DhcpListView.as_view() , name='dhcp_list'),
    path('add', views.DhcpCreateView.as_view(), name='dhcp_add'),
    path('<int:pk>/', views.DhcpView.as_view(), name='dhcp'),
    path('delete', views.DhcpBulkDeleteView.as_view(), name='dhcp_bulk_delete'),
    path('<int:pk>/delete/', views.DhcpDeleteView.as_view(), name='dhcp_delete'),
    path('<int:pk>/edit/', views.DhcpEditView.as_view(), name='dhcp_edit'),
    path('import', views.DhcpBulkImportView.as_view(), name='dhcp_import'),
   

    #IP Fixo
    path('ipfixo/', views.IpfixoListView.as_view() , name='ipfixo_list'),
    path('ipfixo/add/', views.IpfixoCreateView.as_view(), name='ipfixo_add'),
    path('ipfixo/<int:pk>/', views.IpfixoView.as_view(), name='ipfixo'),
    path('ipfixo/delete/', views.IpfixoBulkDeleteView.as_view(), name='ipfixo_bulk_delete'),
    path('ipfixo/<int:pk>/delete/', views.IpfixoDeleteView.as_view(), name='ipfixo_delete'),
    path('ipfixo/<int:pk>/edit/', views.IpfixoEditView.as_view(), name='ipfixo_edit'),
    path('ipfixo/import/', views.IpfixoBulkImportView.as_view(), name='ipfixo_import'),



] 
