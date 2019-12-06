from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from ..models.todo import Todo
from .forms.todo import TodoForm

class TodosUpdate(View):
    form_class = TodoForm
    initial = {'task': 'Write your task'}
    template_name = 'todos.html'

    def get(self, request, id, *args, **kwargs):
        todo = Todo.objects.get(pk=id)
        form = self.form_class(initial={'task': todo.task})
        print("Updating this id: %s" % (id))
        return render(request, "base.html", {'template_name': 'update.html', 'form': form, 'todo': todo})
