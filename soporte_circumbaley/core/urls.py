from django.urls import path
from core.views import HomePageView, SampleView

urlpatterns = [
    path('', HomePageView.as_view(), name="base"),
    # path('sample/', SampleView.as_view(), name="sample"),
]
