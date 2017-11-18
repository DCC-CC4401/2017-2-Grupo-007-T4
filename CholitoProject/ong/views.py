from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class IndexView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'ong-estadisticas.html', {})
