from django.db import models
from aplicaciones.categoria.models import Categoria
from django.core.validators import MinValueValidator
# Create your models here.
class Producto (models.Model):
    #Modelo de producto
    MEDIDAS_CHOICES =(
        ('0', 'Grs'),
        ('1', 'Kgs'),
        ('2', 'Cm3'),
        ('3', 'Mls'),
        ('4', 'Lts'),
    )
    nombre = models.CharField('Nombre', max_length=50)
    id = models.CharField('ID', max_length=50, primary_key=True)
    medida = models.DecimalField('Medida', max_digits=6, decimal_places=2)
    tipo_medida = models.CharField('Tipo de medida', max_length=1, choices=MEDIDAS_CHOICES)
    descripcion = models.TextField('Descripción')  # Campo de texto largo
    precio = models.DecimalField('Precio ($)', max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])  # Campo decimal (10 digitos incluyendo dec)(2 decimales)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    # Relacion entre producto y categoria (De 1 a muchos)
    
    class Meta:
        verbose_name = ('Producto')
        verbose_name_plural = ('Productos')
        ordering = ['nombre']
        unique_together = ('nombre', 'id', 'tipo_medida', 'medida')
    
    def __str__(self):
        return self.id+' - '+self.nombre
