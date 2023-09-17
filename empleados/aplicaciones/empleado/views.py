from django.shortcuts import render
# Create your views here.
from django.views.generic import TemplateView, ListView

class IndexView (TemplateView):           # TemplateView es para algo estático y ListView para recuperar de base de datos
    template_name= 'empleado/home.html'
    
class ProductosView (TemplateView):           # TemplateView es para algo estático y ListView para recuperar de base de datos
    template_name= 'empleado/productos.html'

class PruebaListVIew (ListView):   # Es una clase basada en vistas proporcionadas por el módulo django.views.generic
    template_name = 'empleado/lista.html'
    queryset = ['A','B','C']
    context_object_name = 'lista_prueba'

