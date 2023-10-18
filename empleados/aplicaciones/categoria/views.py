from django.shortcuts import render
from aplicaciones.categoria.models import Categoria
def categorias (request):
    categorias = Categoria.objects.all()
    return render(request, 'categoria/categoria.html', {
        'categorias': categorias
    })
