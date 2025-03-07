from django.db import models


# AQUI CREAREMOS NUESTROS MODELOS EN FORMA DE CLASES
# Se pueden crear tablas como lo requiera la aplicacion y el proyecto

            # Heredamos los modelos de django
class Project(models.Model):
    # Atributos = Columnas
    name = models.CharField(max_length=200) # Caracteres = Varchar

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE) # Llave foranea de proyecto,
    # Se eliminan las tareas si se elimina el proyecto
    done = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.project.name.title()} - {self.title}'