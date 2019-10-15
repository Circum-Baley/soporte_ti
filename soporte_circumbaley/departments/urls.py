from django.urls import path
from departments.views import DepartmentCreateView, DepartmentsDetailView, DepartmentUpdateView, DepartmentListView, \
    DepartmentDeleteView

departments_patterns = ([
                            path('', DepartmentListView.as_view(), name="departments"),
                            path('<int:pk>/<slug:slug>/', DepartmentsDetailView.as_view(), name="department"),
                            path('create/', DepartmentCreateView.as_view(), name="create"),
                            path('update/<int:pk>/', DepartmentUpdateView.as_view(), name="update"),
                            path('delete/<int:pk>/', DepartmentDeleteView.as_view(), name="delete"),
                        ], 'departments')
