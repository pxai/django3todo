from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from ..models.todo import Todo
from .forms.todo import TodoForm

class TodosUpdate(View):
    model = Todo
    form_class = TodoForm
    #initial = {'task': 'Write your task'}

    def get(self, request, id, *args, **kwargs):
        todo = Todo.objects.get(pk=id)
        form = self.form_class(initial={'task': todo.task, 'id': todo.id}) # by hand
        # form  = TodoForm(request.POST, instance=todo)
        print("Updating this id: %s" % (id))
        return render(request, "base.html", {'template_name': 'update.html', 'form': form, 'todo': todo})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            todo = Todo(id=form.cleaned_data['id'],task=form.cleaned_data['task'])
            todo.save()
            print("Form is valid!!")
            return HttpResponseRedirect('/todos')

        return render(request, "base.html", {'template_name': 'update.html', 'form': form})