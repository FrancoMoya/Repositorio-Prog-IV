from django.contrib import admin
from .models import Empleado, Habilidades

# Register your models here.

admin.site.register(Habilidades)
# Para poder manejar los models

class EmpleadoAdmin (admin.ModelAdmin):
    list_display = (
        'nombre',
        'apellido',        # Para poder listar los datos que quiero en tabla
        'trabajo',
        'departamento'
    )
admin.site.register(Empleado, EmpleadoAdmin)