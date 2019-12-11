from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)
from django.core.urlresolvers import reverse_lazy

from ..models import TaskType


class TaskTypeList(ListView):
    model = TaskType


class TaskTypeDetail(DetailView):
    model = TaskType


class TaskTypeCreation(CreateView):
    model = TaskType
    success_url = reverse_lazy('TaskTypes:list')
    fields = ['name', 'description']


class TaskTypeUpdate(UpdateView):
    model = TaskType
    success_url = reverse_lazy('TaskTypes:list')
    fields = ['name', 'description']


class TaskTypeDelete(DeleteView):
    model = TaskType
    fields = ['name', 'description']