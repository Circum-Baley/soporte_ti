from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Department
from .form import DepartmentForm
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


class DepartmentListView(ListView):
    model = Department


class DepartmentsDetailView(DetailView):
    model = Department


@method_decorator(staff_member_required, name="dispatch")
class DepartmentCreateView(CreateView):
    model = Department
    form_class = DepartmentForm
    success_url = reverse_lazy('departments:departments')


@method_decorator(staff_member_required, name="dispatch")
class DepartmentUpdateView(UpdateView):
    model = Department
    form_class = DepartmentForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('departments:update', args=[self.object.id]) + '?ok'


@method_decorator(staff_member_required, name="dispatch")
class DepartmentDeleteView(DeleteView):
    model = Department
    success_url = reverse_lazy('departments:departments')
