"""soporte_circumbaley URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from categories.urls import categories_patterns
from core.views import LinePageView
from core import views
from core.views import LinePageView, TestPageView
from departments.urls import departments_patterns
from devices.urls import devices_patterns
from documents.urls import documents_patterns
from profiles.urls import profiles_patterns
from django.conf import settings
from messenger.urls import messenger_patterns
from services.urls import services_patterns
from suppliers.urls import suppliers_patterns
from supplies.urls import supplies_patterns

urlpatterns = [
    path('chartdevices/', views.chartDevices, name="chartdevices"),
    path('population/', views.chartPopulation, name="population"),
    path('line/', LinePageView.as_view(), name="line"),
    path('categories/', include(categories_patterns)),
    # path de insumos
    path('supplies', include(suppliers_patterns)),
    # path de proveedor
    path('suppliers/', include(supplies_patterns)),
    # path de servicios
    path('services/', include(services_patterns)),
    # path de documents
    path('documents/', include(documents_patterns)),
    # path de messenger
    path('messenger/', include(messenger_patterns)),
    # path del urls del Core
    path('', include('core.urls')),
    path('profiles/', include(profiles_patterns)),
    # path del urls del Profile
    path('devices/', include(devices_patterns)),
    # path de Adninistracion
    path('admin/', admin.site.urls),
    # Path Auth
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),
    path('departments', include(departments_patterns)),
]

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
