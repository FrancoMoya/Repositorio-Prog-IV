from django.contrib import admin
from .models import Producto
# Register your models here.
class ProductoAdmin (admin.ModelAdmin):
    list_display = (
        'id',
        'categoria',
        'nombre',
        'medida',
        'tipo_medida',    # Para poder listar los datos que quiero en tabla
        'precio',
        'total_stock',
    )
    search_fields = ['nombre','id']
    list_filter = ['categoria']
    list_editable = ['precio']
admin.site.register(Producto,ProductoAdmin)