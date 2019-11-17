from django.http import HttpResponse
from django.views import View
from django.shortcuts import render

class About(View):
    author = "Pello Altadill"
    def get(self, request):
        return render(request, 'about.html', {'author': self.author})