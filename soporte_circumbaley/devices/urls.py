from django.urls import path
from devices.views import DeviceCreateView, DevicesDetailView, DeviceUpdateView, DeviceListView, DeviceDeleteView

devices_patterns = ([
                        path('', DeviceListView.as_view(), name="devices"),
                        path('<int:pk>/<slug:slug>/', DevicesDetailView.as_view(), name="device"),
                        path('create/', DeviceCreateView.as_view(), name="create"),
                        path('update/<int:pk>/', DeviceUpdateView.as_view(), name="update"),
                        path('delete/<int:pk>/', DeviceDeleteView.as_view(), name="delete"),
                    ], 'devices')
