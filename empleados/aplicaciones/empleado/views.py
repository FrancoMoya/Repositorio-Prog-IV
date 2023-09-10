from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView

class IndexView (TemplateView):
    template_name= 'empleado/home.html'

class PruebaListVIew (ListView):
    template_name = 'empleado/lista.html'
    queryset = ['A','B','C']
    context_object_name = 'lista_prueba'
