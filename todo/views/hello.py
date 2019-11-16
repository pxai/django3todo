from django.http import HttpResponse
from django.views import View

class Hello(View):
    def get(self, request):
        # <view logic>
        return HttpResponse('Well hello lady')