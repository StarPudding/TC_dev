from django.urls import path
from all_test.src.monitor.interface import wms_app_monitor
from all_test.src.monitor import views

urlpatterns = [
    path(r'login/', wms_app_monitor.login),
    path(r'show_monitor_info/', wms_app_monitor.show_monitor_info),
    path(r'get_monitor_status/', wms_app_monitor.get_monitor_status),
    path(r'get_all_warehouse/', wms_app_monitor.get_all_warehouse),
    path(r'getMonitorInfo/', views.getMonitorInfo),
    path(r'getAllWarehouse/', views.getAllWarehouse)
]
