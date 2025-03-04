from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    email = models.EmailField(unique=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.nombre