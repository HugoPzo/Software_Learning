from django.urls import path  # Importa la función `path` para definir rutas en Django
from . import views  # Importa el módulo `views.py` del mismo directorio


# urlpatterns - debe mantener ese nombre
#
urlpatterns = [
    path('', views.mi_vista, name='home')
]

# urlpatterns es una lista de rutas que Django usa para determinar qué
#                               vista ejecutar según la URL solicitada.


# La línea path('', views.render, name='home') indica:

# '' → La URL base del sitio (ejemplo: http://tudominio.com/).
# views.mi_vista → Llama a la función mi_vista en views.py cuando un usuario accede a la URL base.
# name='home' → Un nombre opcional para referirse a esta ruta en el código.
