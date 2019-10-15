from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Service
from .form import ServicesForm
from django.shortcuts import redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator


class StaffRequiredMixin(object):
    """
    Este mixin requerira que el usuario sea miembro del stuff
    """

    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)


class ServiceListView(ListView):
    model = Service


class ServicesDetailView(DetailView):
    model = Service


@method_decorator(staff_member_required, name="dispatch")
class ServiceCreateView(CreateView):
    model = Service
    form_class = ServicesForm
    success_url = reverse_lazy('services:services')


@method_decorator(staff_member_required, name="dispatch")
class ServiceUpdateView(UpdateView):
    model = Service
    form_class = ServicesForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('services:update', args=[self.object.id]) + '?ok'


@method_decorator(staff_member_required, name="dispatch")
class ServiceDeleteView(DeleteView):
    model = Service
    success_url = reverse_lazy('services:services')
