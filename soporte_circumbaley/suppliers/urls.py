from django.urls import path
from .views import SupplierCreateView, SuppliersDetailView, SupplierUpdateView, SupplierListView, SupplierDeleteView

suppliers_patterns = ([
                          path('', SupplierListView.as_view(), name="suppliers"),
                          path('<int:pk>/<slug:slug>/', SuppliersDetailView.as_view(), name="supplier"),
                          path('create/', SupplierCreateView.as_view(), name="create"),
                          path('update/<int:pk>/', SupplierUpdateView.as_view(), name="update"),
                          path('delete/<int:pk>/', SupplierDeleteView.as_view(), name="delete"),
                      ], 'suppliers')
