from django.db.models import Count, Q
from django.shortcuts import render
from django.views.generic.base import TemplateView

from devices.models import Devices
from registration.models import Profile
from messenger.models import Message


# Create your views here.

class HomePageView(TemplateView):
    template_name = "core/index.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'name': "Ejemplo de la primera Web"})


class LinePageView(TemplateView):
    template_name = 'charts/line-boundaries.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.get_template_names())


class TestPageView(TemplateView):
    template_name = 'charts/chartPopulation.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.get_template_names())


class SampleView(TemplateView):
    template_name = "core/sample.html"


def chartPopulation(request):
    return render(request, 'charts/chartPopulation.html')


def chartDevices(request):
    dataset = Devices.objects \
        .values('name') \
        .annotate(is_new_count=Count('name', filter=Q(is_new=True)),
                  not_is_new_count=Count('name', filter=Q(is_new=False))) \
        .order_by('created')
    return render(request, 'charts/chartDevices.html', {'dataset': dataset})


def ticket_class_view_2(request):
    dataset = Profile.objects \
        .values('ticket_class') \
        .annotate(survived_count=Count('ticket_class', filter=Q(survived=True)),
                  not_survived_count=Count('ticket_class', filter=Q(survived=False))) \
        .order_by('ticket_class')

    categories = list()
    survived_series = list()
    not_survived_series = list()

    for entry in dataset:
        categories.append('%s Class' % entry['ticket_class'])
        survived_series.append(entry['survived_count'])
        not_survived_series.append(entry['not_survived_count'])

    return render(request, 'ticket_class_2.html', {
        'categories': json.dumps(categories),
        'survived_series': json.dumps(survived_series),
        'not_survived_series': json.dumps(not_survived_series)
    })
