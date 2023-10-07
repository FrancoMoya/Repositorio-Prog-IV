from django.db import models
from aplicaciones.producto.models import Producto
from aplicaciones.detalle_pedido.models import DetallePedido
from django.contrib.auth.models import User

class Carrito (models.Model):
    id_carritos = models.BigAutoField (primary_key=True)
    usuario = models.OneToOneField (User, on_delete=models.CASCADE)
    productos = models.ManyToManyField (Producto, through = 'CarritoProducto')
    class Meta:
        verbose_name = ('Carrito')
        verbose_name_plural = ('Carritos')
        ordering = ['usuario']
        
    def __str__(self):
        return f"ID:{self.id_carritos} - User:{self.usuario.username}"
class CarritoProducto (models.Model):
    id_carrito = models.ForeignKey (Carrito, on_delete=models.CASCADE)
    id_producto = models.ForeignKey (Producto, on_delete=models.CASCADE)
    id_detalle_pedido = models.ForeignKey (DetallePedido, on_delete=models.CASCADE)
    cantidad = models.PositiveBigIntegerField ('Cantidad', default=1)
    estado = models.BooleanField ('Estado activo', default=True)
