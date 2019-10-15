from django.urls import path
from .views import ServiceCreateView, ServicesDetailView, ServiceUpdateView, ServiceListView, ServiceDeleteView

services_patterns = ([
                         path('', ServiceListView.as_view(), name="services"),
                         path('<int:pk>/<slug:slug>/', ServicesDetailView.as_view(), name="service"),
                         path('create/', ServiceCreateView.as_view(), name="create"),
                         path('update/<int:pk>/', ServiceUpdateView.as_view(), name="update"),
                         path('delete/<int:pk>/', ServiceDeleteView.as_view(), name="delete"),
                     ], 'services')
