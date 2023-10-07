from django.contrib import admin
from .models import Descuentos, DescuentoProducto, DescuentoCarrito, DescuentoUsuario

@admin.register(Descuentos)
class DescuentosAdmin (admin.ModelAdmin):
    list_display = (
        'nombre',
        'porcentaje',
        'valor',
        'mostrar_productos',
        'mostrar_carritos',
        'mostrar_usuarios',
    )
    def mostrar_productos(self, obj):
        return ", ".join([producto.nombre for producto in obj.productos.all()])
    mostrar_productos.short_description = 'Productos'
    
    def mostrar_carritos(self, obj):
        # Convierte los IDs de carritos en cadenas y únelos
        carrito_ids = [str(carrito.id_carritos) for carrito in obj.carritos.all()]
        return ", ".join(carrito_ids)
    mostrar_carritos.short_description = 'ID Carritos'
    
    def mostrar_usuarios(self, obj):
        return ", ".join([usuario.username for usuario in obj.usuarios.all()])
    mostrar_usuarios.short_description = 'Usuarios'
    
@admin.register(DescuentoProducto)
class DescuentoProductoAdmin (admin.ModelAdmin):
    list_display= (
        'id_descuento',
        'id_producto',
        'fecha_venc',
    )
    
@admin.register(DescuentoCarrito)
class DescuentoCarritoAdmin (admin.ModelAdmin):
    list_display= (
        'id_descuento',
        'id_carrito',
        'fecha_venc',
    )

@admin.register(DescuentoUsuario)
class DescuentoUsuarioAdmin (admin.ModelAdmin):
    list_display= (
        'id_descuento',
        'id_usuario',
        'fecha_venc',
    )