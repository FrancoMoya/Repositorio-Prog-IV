from django.db import models

# Create your models here.
# titulo charfield string
# subtitulo charfield string

class Prueba (models.Model):
    titulo = models.CharField(max_length=30)
    subtitulo = models.CharField(max_length=30)
