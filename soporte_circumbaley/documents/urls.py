from django.urls import path
from .views import DocumentCreateView, DocumentsDetailView, DocumentUpdateView, DocumentListView, DocumentDeleteView

documents_patterns = ([
                          path('', DocumentListView.as_view(), name="documents"),
                          path('<int:pk>/<slug:slug>/', DocumentsDetailView.as_view(), name="document"),
                          path('create/', DocumentCreateView.as_view(), name="create"),
                          path('update/<int:pk>/', DocumentUpdateView.as_view(), name="update"),
                          path('delete/<int:pk>/', DocumentDeleteView.as_view(), name="delete"),
                      ], 'documents')
