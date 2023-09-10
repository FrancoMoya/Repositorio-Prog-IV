from django.db import models

# Create your models here.
class Departamento (models.Model):
    nombre = models.CharField('Nombre', max_length=35, blank=True)    #Max_length ancho  | El 1er valor es la etiqueta
    sigla = models.CharField('Sigla', max_length=10)                  #El blank si permite o no blancos
    activo = models.BooleanField('¿Está activo?', default= False)     #Un campo boolean  | Si por defecto venia activo o no
    piso = models.CharField('Piso', max_length=5, blank=True)
    oficina = models.CharField('Oficina N°', max_length=10, blank=True)
    
    class Meta:
        verbose_name = 'Empresa'    # Para cambiar el nombre de la clase en singular
        verbose_name_plural = ('Departamentos')   # Para cambiar el nombre de la clase en plural
        ordering = ['nombre']  # Se debe poner dentro de las comillas la var del atributo
        unique_together = ('nombre', 'sigla')
    
    def __str__(self):
        return self.nombre+' - '+self.sigla+' - '+self.piso+' - '+self.oficina