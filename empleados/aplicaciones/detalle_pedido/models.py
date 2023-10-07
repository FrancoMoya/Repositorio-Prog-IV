from django.db import models
from aplicaciones.pedido.models import Pedido
class DetallePedido (models.Model):
    id_detalle_pedido = models.BigAutoField('ID',primary_key=True)
    cantidad = models.IntegerField('Cantidad')
    precio_unitario = models.DecimalField('Precio unitario', max_digits=10, decimal_places=2)
    pedido = models.OneToOneField(Pedido, on_delete=models.CASCADE)
    class Meta:
        verbose_name = ('Detalle de Pedido')
        verbose_name_plural = ('Detalles de Pedidos')
        ordering = ['id_detalle_pedido']
    
    def __str__(self):
        return f"{self.id_detalle_pedido} - {self.pedido.id_pedido} - User: {self.pedido.usuario.username}"