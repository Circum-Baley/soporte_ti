from django.contrib.auth.models import User
from django.http import Http404, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from .models import Thread, Message

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.
@method_decorator(login_required, name="dispatch")
class ThreadListView(TemplateView):
    model = Thread
    template_name = 'messenger/thread_list.html'

    # def get_queryset(self):
    #     queryset = super(ThreadListView, self).get_queryset()
    #     return queryset.filter(users=self.request.user)


@method_decorator(login_required, name="dispatch")
class ThreadDetailView(DetailView):
    model = Thread

    def get_objects(self):
        obj = super(ThreadDetailView, self).get_objects()
        if self.request.user not in obj.users.all():
            raise Http404()
        return obj


def add_message(request, pk):
    # print(request.GET)
    json_response = {'created': False}
    if request.user.is_authenticated:
        content = request.GET.get('content', None)
        if content:
            thread = get_object_or_404(Thread, pk=pk)
            message = Message.objects.create(user=request.user, content=content)
            thread.messages.add(message)
            json_response['created'] = True
            if len(thread.messages.all()) is 1:
                json_response['first'] = True
    else:
        raise Http404("User No Authenticated")
    return JsonResponse(json_response)


@login_required
def start_thread(request, username):
    user = get_object_or_404(User, username=username)
    thread = Thread.objects.find_or_create(user, request.user)
    return redirect(reverse_lazy('messenger:detail', args=[thread.pk]))
