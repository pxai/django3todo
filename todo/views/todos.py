from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from 

from .forms.todo import TodoForm

class Todos(View):
    form_class = TodoForm
    initial = {'key': 'value'}
    template_name = 'todos.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>

            print("Form is valid!!")
            return HttpResponseRedirect('/todos')

        return render(request, self.template_name, {'form': form})