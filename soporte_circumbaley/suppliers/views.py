from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Supplier
from .form import SuppliersForm
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator


class StaffRequiredMixin(object):
    """
    Este mixin requerira que el usuario sea miembro del stuff
    """

    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)


class SupplierListView(ListView):
    model = Supplier


class SuppliersDetailView(DetailView):
    model = Supplier


@method_decorator(staff_member_required, name="dispatch")
class SupplierCreateView(CreateView):
    model = Supplier
    form_class = SuppliersForm
    success_url = reverse_lazy('suppliers:suppliers')


@method_decorator(staff_member_required, name="dispatch")
class SupplierUpdateView(UpdateView):
    model = Supplier
    form_class = SuppliersForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('suppliers:update', args=[self.object.id]) + '?ok'


@method_decorator(staff_member_required, name="dispatch")
class SupplierDeleteView(DeleteView):
    model = Supplier
    success_url = reverse_lazy('suppliers:suppliers')
