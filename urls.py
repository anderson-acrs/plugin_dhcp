from django.urls import path, include
from . import views

""" comentario """
app_name = 'dhcpd'
urlpatterns = [
    path('', views.DhcpListView.as_view() , name='dhcp_list'),
    path('add', views.DhcpCreateView.as_view(), name='dhcp_add'),
    path('<int:pk>/', views.DhcpView.as_view(), name='dhcp'),
    path('delete', views.DhcpBulkDeleteView.as_view(), name='dhcp_bulk_delete'),
    path('<int:pk>/delete/', views.DhcpDeleteView.as_view(), name='dhcp_delete'),
    path('<int:pk>/edit/', views.DhcpEditView.as_view(), name='dhcp_edit'),
    # path('<int:pk/delete/>', views.DhcpBulkDeleteView.as_view(), name='dhcp_bulk_delete'),
    # path('edit/<int:pk>/', views.DhcpEditView.as_view(), name='dhcp_edit'),
    # path('api/', include('appview.api.urls')),
    # path('random/', views.RandomSwitchView.as_view(), name='random_switch'),

] 
