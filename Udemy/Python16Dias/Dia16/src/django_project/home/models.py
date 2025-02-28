from tkinter.constants import CASCADE

from django.db import models
# DJANGO Y TIENE CREADAS ALGUNAS TABLAS - EN ESTE CASO USAREMOS LAS DE USUARIOS
from django.contrib.auth.models import User

# MODELOS DE BASE DE DATOS EN DJANGO

# EN ESTE EJERCICIO SE REALIZARA UNA TABLA DE TAREAS COMPLETADAS O POR REALIZAR

# Create your models here.
# CREAMOS CLASES - LAS CUALES VAN A SER TABLAS DE BASES DE DATOS, SUS ATRIBUTOS SON LAS COLUMNAS Y CAMPOS

class Tarea(models.Model):
    # Un usuario puede crear varias tareas
            # Asociamos nuestros modelos de User

    usuario = models.ForeignKey(User,
                                on_delete=models.CASCADE, # Se eliminan todas las tareas creadas por este usuario si es eliminado
                                null=True,  # El valor de usuario puede estar vacio o el registro puede estar en blanco
                                blank=True)
    titulo = models.CharField(max_length=75) # Area de linea de texto con un maximo de 75 caracteres
    descricion = models.TextField(null=True, blank=True)
    completo = models.BooleanField(default=False) # Marcamos como default que la casilla no este seleccionada
    creado = models.DateTimeField(auto_now_add=True) # Se genera automaticamente la fecha de la creacion de la tarea


    def __str__(self):
        return self.titulo


    class Meta:
        # Manera de ordenacion de las tareas en nuestra tabla
        ordering = ['completo'] # Una vez completas se mandan al final de la lista


# Ahora debemos migrar nuestra tabla a la base de datos de nuestro sitio

