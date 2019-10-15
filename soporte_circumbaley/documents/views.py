from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Document
from .form import DocumentsForm
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


class DocumentListView(ListView):
    model = Document


class DocumentsDetailView(DetailView):
    model = Document


@method_decorator(staff_member_required, name="dispatch")
class DocumentCreateView(CreateView):
    model = Document
    form_class = DocumentsForm
    success_url = reverse_lazy('documents:documents')


@method_decorator(staff_member_required, name="dispatch")
class DocumentUpdateView(UpdateView):
    model = Document
    form_class = DocumentsForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('documents:update', args=[self.object.id]) + '?ok'


@method_decorator(staff_member_required, name="dispatch")
class DocumentDeleteView(DeleteView):
    model = Document
    success_url = reverse_lazy('documents:documents')
