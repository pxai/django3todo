from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from ..models.todo import Todo
from .forms.todo import TodoForm

class TodosUpdate(View):
    form_class = TodoForm
    initial = {'task': 'Write your task'}
    template_name = 'todos.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        todos = Todo.objects.all()
        print(todos)
        return render(request, "base.html", {'template_name': self.template_name, 'form': form, 'todos': todos})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            todo = Todo(task=form.cleaned_data['task'])
            todo.save()
            print("Form is valid!!")
            return HttpResponseRedirect('/todos')

        return render(request, "base.html", {'template_name': self.template_name, 'form': form})

    def update(self, request, id, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        todo = Todo.objects.get(id)
        print("Im NOT IN UPDATE??")
        return render(request, "base.html", {'template_name': 'update.html', 'form': form, 'todo': todo})
