from django.urls import path
from .views import SupplyCreateView, SuppliesDetailView, SupplyUpdateView, SupplyListView, SupplyDeleteView

supplies_patterns = ([
                         path('', SupplyListView.as_view(), name="supplies"),
                         path('<int:pk>/<slug:slug>/', SuppliesDetailView.as_view(), name="supply"),
                         path('create/', SupplyCreateView.as_view(), name="create"),
                         path('update/<int:pk>/', SupplyUpdateView.as_view(), name="update"),
                         path('delete/<int:pk>/', SupplyDeleteView.as_view(), name="delete"),
                     ], 'supplies')
