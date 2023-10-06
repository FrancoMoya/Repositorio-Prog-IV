from django.db import models
# Create your models here.
class Pedido (models.Model):
    TIPOS_PAGOS_CHOICES=(
        ('0','Mercado Pago'),
        ('1','Tarjeta de crédito'),
        ('2','Tarjeta de débito'),
    )
    
    id_pedido = models.BigAutoField(primary_key=True)
    total = models.DecimalField('Total a pagar',max_digits=20, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)
    #usuario = models.OneToOneField (Usuario, on_delete=models.CASCADE)
    medio_de_pago = models.CharField ('Medio de Pago', max_length=1, choices=TIPOS_PAGOS_CHOICES)
    class Meta:
        verbose_name = ('Pedido')
        verbose_name_plural = ('Pedidos')
        ordering = ['fecha']
    
    def __str__(self):
        return f"{self.total} - {self.medio_de_pago} - {self.fecha}"
