
from django.db import models

class Solicitud(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
