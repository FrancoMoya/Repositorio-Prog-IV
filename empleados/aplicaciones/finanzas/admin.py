from django.contrib import admin
from .models import Finanzas

@admin.register(Finanzas)
class FinanzasAdmin (admin.ModelAdmin):
    
    def finanzas_departamento_display (self, obj):
        return ", ".join([departamento.nombre for departamento in obj.Departamentos.all()])
    finanzas_departamento_display.short_description = 'Departamentos'
    
    def finanzas_descuento_display (self, obj):
        descuento_ids = [str(descuento.id_descuentos) for descuento in obj.Descuentos.all()]
        return ", ".join(descuento_ids)
    finanzas_descuento_display.short_description = 'Descuentos'
    
    def finanzas_producto_display (self, obj):
        return ", ".join([producto.nombre for producto in obj.Productos.all()])
    finanzas_producto_display.short_description = 'Productos'
    
    def finanzas_pedido_display (self, obj):
        pedido_total = [str(pedido.total) for pedido in obj.Pedidos.all()]
        return ", ".join(pedido_total)
    finanzas_pedido_display.short_description = 'Pedidos'
    
    list_display = (
        'tipo_reporte',
        'finanzas_departamento_display',
        'finanzas_pedido_display',
        'finanzas_producto_display',
        'finanzas_descuento_display',
        'descripcion',
        'fecha',
    )
    
    readonly_fields=['fecha']