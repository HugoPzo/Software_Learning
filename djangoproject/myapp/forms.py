from django import forms
from django.urls import reverse_lazy
from .models import Task

# CREAMOS FORMULARIOS CON CODIGO DE PYTHON

# Toda esta clase la interpreta y la transforma en codigo HTML
class CreateNewTask(forms.Form):
    title = forms.CharField(label='Titulo de tarea', max_length=200)
    description = forms.CharField(widget=forms.Textarea, label="Descripcion de la tarea")


class CreateNewProject(forms.Form):
    name = forms.CharField(label='Nombre del proyecto', max_length=50)
