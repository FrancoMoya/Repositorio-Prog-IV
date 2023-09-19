from django.db import models
from aplicaciones.departamento.models import Departamento # Importo departamento
# Create your models here.
# titulo charfield string
# subtitulo charfield string
class Empleado (models.Model):
    #Modelo de empleado
    JOB_CHOICES =(
        ('0', 'Contador'),
        ('1', 'Administrativo'),
        ('2', 'Desarrollador'),
        ('3', 'Analista Funcional'),
        ('4', 'Otro'),
    )
    nombre = models.CharField('Nombre', max_length=50)
    apellido = models.CharField('Apellido', max_length=50)
    trabajo = models.CharField('Puesto', max_length=1, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    # Relacion entre empleado y departamento (De 1 a muchos)
    
    # habilidad = models.ManyToManyField(Habilidades)
    # Relacion entre empleado y habilidades (De muchos a muchos)
    class Meta:
        verbose_name = ('Mi empleado')
        verbose_name_plural = ('Empleados de la empresa')
        ordering = ['nombre',]
        unique_together = ('nombre', 'departamento')
    
    def __str__(self):
        return self.nombre+' - '+self.apellido