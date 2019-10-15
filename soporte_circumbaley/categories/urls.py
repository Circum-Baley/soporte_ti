from django.urls import path
from .views import CategoryCreateView, CategoriesDetailView, CategoryUpdateView, CategoryListView, CategoryDeleteView

categories_patterns = ([
                           path('', CategoryListView.as_view(), name="categories"),
                           path('<int:pk>/<slug:slug>/', CategoriesDetailView.as_view(), name="category"),
                           path('create/', CategoryCreateView.as_view(), name="create"),
                           path('update/<int:pk>/', CategoryUpdateView.as_view(), name="update"),
                           path('delete/<int:pk>/', CategoryDeleteView.as_view(), name="delete"),
                       ], 'categories')
