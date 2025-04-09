from django.db import models

class Actividad(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    profesor = models.CharField(max_length=100)
    aula = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
