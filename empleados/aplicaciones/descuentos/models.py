from django.db import models
from aplicaciones.producto.models import Producto
from aplicaciones.carrito.models import Carrito
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

def validate_two_digit(value):
    if not (0 <= value <= 99):
        raise ValidationError("El porcentaje debe ser un número de dos dígitos (0-99).")

class Descuentos (models.Model):
    id_descuentos = models.BigAutoField (primary_key=True)
    nombre = models.CharField('Nombre del descuento', max_length=45)
    porcentaje = models.IntegerField('Porcentaje de descuento', validators=[validate_two_digit], null=True, blank=True)
    valor = models.IntegerField('Valor de descuento', null=True, blank=True)
    productos = models.ManyToManyField (Producto, through = 'DescuentoProducto')
    carritos = models.ManyToManyField (Carrito, through = 'DescuentoCarrito')
    usuarios = models.ManyToManyField (User, through = 'DescuentoUsuario')
    class Meta:
        verbose_name = ('Descuento')
        verbose_name_plural = ('Descuentos')
        ordering = ['nombre']
        
    def __str__(self):
        return f"ID:{self.id_descuentos} - Tipo: {self.nombre}"
    
class DescuentoProducto (models.Model):
    id_descuento = models.ForeignKey (Descuentos, on_delete=models.CASCADE)
    id_producto = models.ForeignKey (Producto, on_delete=models.CASCADE)
    fecha_venc = models.DateField('Fecha de vencimiento')
    class Meta:
        verbose_name = ('Descuento a productos')
        verbose_name_plural = ('Descuentos de Productos')
        ordering = ['fecha_venc']
    
    def __str__(self):
        return f"{self.id_descuento} - {self.id_producto}"
    
class DescuentoCarrito (models.Model):
    id_descuento = models.ForeignKey (Descuentos, on_delete=models.CASCADE)
    id_carrito= models.ForeignKey (Carrito, on_delete=models.CASCADE)
    fecha_venc = models.DateField('Fecha de vencimiento')
    class Meta:
        verbose_name = ('Descuento a Carritos')
        verbose_name_plural = ('Descuentos de Carritos')
        ordering = ['fecha_venc']
    
    def __str__(self):
        return f"{self.id_descuento} - {self.id_carrito}"

class DescuentoUsuario (models.Model):
    id_descuento = models.ForeignKey (Descuentos, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey (User, on_delete=models.CASCADE)
    fecha_venc = models.DateField('Fecha de vencimiento')
    class Meta:
        verbose_name = ('Descuento a Usuarios')
        verbose_name_plural = ('Descuentos de Usuarios')
        ordering = ['fecha_venc']
    
    def __str__(self):
        return f"{self.id_descuento} - {self.id_usuario}"