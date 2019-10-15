from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Devices
from .form import DevicesForm
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


class DeviceListView(ListView):
    model = Devices


class DevicesDetailView(DetailView):
    model = Devices


@method_decorator(staff_member_required, name="dispatch")
class DeviceCreateView(CreateView):
    model = Devices
    form_class = DevicesForm
    success_url = reverse_lazy('devices:devices')


@method_decorator(staff_member_required, name="dispatch")
class DeviceUpdateView(UpdateView):
    model = Devices
    form_class = DevicesForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('devices:update', args=[self.object.id]) + '?ok'


@method_decorator(staff_member_required, name="dispatch")
class DeviceDeleteView(DeleteView):
    model = Devices
    success_url = reverse_lazy('devices:devices')
