from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from ..models.todo import Todo


class TodosDelete(View):
    model = Todo

    def get(self, request, id, *args, **kwargs):
        todo = Todo.objects.get(pk=id)
        todo.delete()
        print("Removed this id: %s" % (id))

        return HttpResponseRedirect('/todos')
