from django.db import models
"""from aplicaciones.producto.models import Producto
# Create your models here.
class Carrito (models.Model):
    #usuario = models.OneToOneField (Usuario, on_delete=models.CASCADE)
    productos = models.Model (Producto, through = 'CarritoProducto')
    
class CarritoProducto (models.Model):
    id_carrito = models.ForeignKey (Carrito, on_delete=models.CASCADE)
    id_prodcuto = models.ForeignKey (Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveBigIntegerField ('Cantidad', default=1)"""
