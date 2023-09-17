from django.db import models
from aplicaciones.producto.models import Producto
# Create your models here.
class Stock (models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField('Cantidad')
    fecha_venc = models.DateField('Fecha de Vencimiento')
    numero_lote = models.CharField('N° de LOTE',max_length=40)
    
    def __str__(self):
        return f"Stock de {self.producto.nombre} (Lote: {self.numero_lote}, Vence: {self.fecha_venc})"
    class Meta:
        unique_together = ['producto', 'numero_lote']     #evita duplic
        verbose_name = ("Stock")
        verbose_name_plural = ("Stocks")
        ordering = ('fecha_venc',)