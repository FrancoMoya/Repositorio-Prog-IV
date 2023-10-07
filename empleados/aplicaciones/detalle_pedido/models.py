from django.db import models
from aplicaciones.pedido.models import Pedido
class DetallePedido (models.Model):
    id_detalle_pedido = models.BigAutoField('ID',primary_key=True)
    cantidad = models.IntegerField('Cantidad')
    precio_unitario = models.DecimalField('Precio unitario', max_digits=10, decimal_places=2)
    pedido = models.OneToOneField(Pedido, on_delete=models.CASCADE)