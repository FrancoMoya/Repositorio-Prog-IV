from django.db import models
from aplicaciones.producto.models import Producto
from aplicaciones.pedido.models import Pedido
from aplicaciones.usuario.models import Customer

class Carrito (models.Model):
    id_carritos = models.BigAutoField (primary_key=True)
    customer = models.OneToOneField (Customer, on_delete=models.CASCADE)
    productos = models.ManyToManyField (Producto, through = 'CarritoProducto')
    class Meta:
        verbose_name = ('Carrito')
        verbose_name_plural = ('Carritos')
        ordering = ['customer']
        
    def __str__(self):
        return f"ID:{self.id_carritos} - User:{self.customer.nombre}"
class CarritoProducto (models.Model):
    id_carrito = models.ForeignKey (Carrito, on_delete=models.CASCADE)
    id_producto = models.ForeignKey (Producto, on_delete=models.CASCADE)
    id_pedido = models.ForeignKey (Pedido, on_delete=models.CASCADE)
    cantidad = models.PositiveBigIntegerField ('Cantidad', default=1)
    estado = models.BooleanField ('Estado activo', default=True)
    fecha_agregado = models.DateTimeField(auto_now_add=True)
    
    @property
    def get_total(self):
        total = self.id_producto.precio * self.cantidad
        return total
