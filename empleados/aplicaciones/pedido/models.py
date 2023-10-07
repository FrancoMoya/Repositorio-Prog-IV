from django.db import models
from django.contrib.auth.models import User
class Pedido (models.Model):
    TIPOS_PAGOS_CHOICES=(
        ('0','Mercado Pago'),
        ('1','Tarjeta de crédito'),
        ('2','Tarjeta de débito'),
    )
    
    id_pedido = models.BigAutoField(primary_key=True)
    total = models.DecimalField('Total a pagar',max_digits=20, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey (User, on_delete=models.CASCADE)
    medio_de_pago = models.CharField ('Medio de Pago', max_length=1, choices=TIPOS_PAGOS_CHOICES)
    class Meta:
        verbose_name = ('Pedido')
        verbose_name_plural = ('Pedidos')
        ordering = ['fecha']
        
    def medio_pago_display(self):
        return dict(self.TIPOS_PAGOS_CHOICES).get(self.medio_de_pago, 'Desconocido')
    def __str__(self):
        # Formatea la fecha y hora sin microsegundos usando strftime()
        formatted_fecha = self.fecha.strftime('%Y-%m-%d %H:%M:%S')
        return f"${self.total} - {self.medio_pago_display()} - {formatted_fecha}"
