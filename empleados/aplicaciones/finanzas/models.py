from django.db import models
from aplicaciones.producto.models import Producto
from aplicaciones.pedido.models import Pedido
from aplicaciones.departamento.models import Departamento
from aplicaciones.descuentos.models import Descuentos

class Finanzas (models.Model):
    CHOICES_REPORTES = (
        ('0', 'Capital'),
        ('1', 'Ganancias'),
        ('2', 'Gastos'),
    )
    
    id_finanzas = models.BigAutoField (primary_key=True)
    fecha = models.DateTimeField(auto_now_add=True)
    tipo_reporte = models.CharField('Tipo de reporte', max_length=1, choices=CHOICES_REPORTES)
    descripcion = models.TextField('Descripción')
    Departamentos = models.ManyToManyField(Departamento, blank=True)
    Pedidos = models.ManyToManyField(Pedido, blank=True)
    Descuentos = models.ManyToManyField(Descuentos, blank=True)
    Productos = models.ManyToManyField(Producto, blank=True)
    class Meta:
        verbose_name = ('Finanzas')
        verbose_name_plural = ('Reportes de Finanzas')
        ordering = ['fecha']
    
    def __str__(self):
        return f"{self.id_finanzas} - {self.fecha}"