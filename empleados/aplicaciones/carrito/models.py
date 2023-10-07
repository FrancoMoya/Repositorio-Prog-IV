from django.db import models
from aplicaciones.producto.models import Producto
from aplicaciones.detalle_pedido.models import DetallePedido
from django.contrib.auth.models import User

class Carrito (models.Model):
    usuario = models.OneToOneField (User, on_delete=models.CASCADE)
    productos = models.ManyToManyField (Producto, through = 'CarritoProducto')
    
class CarritoProducto (models.Model):
    id_carrito = models.ForeignKey (Carrito, on_delete=models.CASCADE)
    id_producto = models.ForeignKey (Producto, on_delete=models.CASCADE)
    id_detalle_pedido = models.ForeignKey (DetallePedido, on_delete=models.CASCADE)
    cantidad = models.PositiveBigIntegerField ('Cantidad', default=1)
    estado = models.BooleanField ('Estado activo', default=True)
