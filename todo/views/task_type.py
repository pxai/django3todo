from django.urls import reverse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)

from ..models import TaskType


class TaskTypeList(ListView):
    model = TaskType
    template_name = "task_type_list.html"


class TaskTypeDetail(DetailView):
    model = TaskType


#class TaskTypeCreation(CreateView):
#    model = TaskType
#    success_url = reverse('TaskTypes:list')
#    fields = ['name', 'description']


#class TaskTypeUpdate(UpdateView):
#    model = TaskType
#    success_url = reverse('TaskTypes:list')
#    fields = ['name', 'description']


#class TaskTypeDelete(DeleteView):
#    model = TaskType
#    fields = ['name', 'description']