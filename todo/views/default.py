from django.http import HttpResponse
from django.views import View
from django.shortcuts import render

class Default(View):
    template_name = 'default.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)