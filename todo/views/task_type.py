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
    template_name = "task_type_list.html" # or it defaults to tasktypes.html

class TaskTypeDetail(DetailView):
    model = TaskType
    template_name = "task_type_detail.html" 

class TaskTypeCreation(CreateView):
    model = TaskType
    success_url = "/task_types"
    template_name = "task_type_form.html" 
    fields = ['name', 'description']


class TaskTypeUpdate(UpdateView):
    model = TaskType
    success_url = "/task_types"
    template_name = "task_type_form.html" 
    fields = ['name', 'description']


class TaskTypeDelete(DeleteView):
    model = TaskType
    template_name = "task_type_form.html" 
    success_url = "/task_types"