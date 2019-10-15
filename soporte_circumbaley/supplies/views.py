from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Supply
from .form import SuppliesForm
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


class SupplyListView(ListView):
    model = Supply


class SuppliesDetailView(DetailView):
    model = Supply


@method_decorator(staff_member_required, name="dispatch")
class SupplyCreateView(CreateView):
    model = Supply
    form_class = SuppliesForm
    success_url = reverse_lazy('supplies:supplies')


@method_decorator(staff_member_required, name="dispatch")
class SupplyUpdateView(UpdateView):
    model = Supply
    form_class = SuppliesForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('supplies:update', args=[self.object.id]) + '?ok'


@method_decorator(staff_member_required, name="dispatch")
class SupplyDeleteView(DeleteView):
    model = Supply
    success_url = reverse_lazy('supplies:supplies')
