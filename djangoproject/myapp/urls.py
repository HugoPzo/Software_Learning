from django.urls import path

# Importacion de views
from . import views

urlpatterns = [
    path('', views.home, name='home'), # path(ruta, funcion o clase de ejecucion)
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('tasks/', views.tasks, name='tasks'),
    path('form_tasks/', views.form_tasks, name='form-tasks'),
    path('form-project/', views.new_project,  name='form-project')
]