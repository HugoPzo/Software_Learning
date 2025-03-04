from django.urls import path  # Importa la función `path` para definir rutas en Django
from .views import ListaPendientes   # Importa el módulo `views.py` del mismo directorio
from .views import DetalleTarea # Importamos los detalles
from .views import CrearTarea # Importamos las creaciones de lista
from .views import EditarTarea # Importamos la edicion de la lista
from .views import EliminarTarea # Importamos la eliminacion de la lista
from .views import Logueo # Importamos el logueo
from .views import custom_logout # Importacion de metodo para desloguear
from .views import Registrar # Importamos clase para registrar nuevo usuario
from django.contrib.auth.views import LogoutView # Importamos el logout


# urlpatterns - debe mantener ese nombre
# Opcion por archivo importado
# urlpatterns = [path('', views.mi_vista, name='home')]

# Por clases, se muestra la clase como una vista - 'name' es el nombre que usaremos para dirigir a esa ruta
urlpatterns = [path('', ListaPendientes.as_view(), name='home'),
               path('login/', Logueo.as_view(), name='login'), # login
               path('logout/', custom_logout, name='logout'), # logout - despues de deslogear, redirigir a login - se debe usar una funcion especial
               path('registrar/', Registrar.as_view(), name='registrar'),
               path('tarea/<int:pk>', DetalleTarea.as_view(), name='tarea'), # Asignamos el endpoint con el numero de la
# tarea (primary key de la tarea)
               path('crear-tarea/', CrearTarea.as_view(), name='crear-tarea'),
               path('editar-tarea/<int:pk>', EditarTarea.as_view(), name='editar-tarea'),
               path('eliminar-tarea/<int:pk>', EliminarTarea.as_view(), name='eliminar-tarea')]

# urlpatterns es una lista de rutas que Django usa para determinar qué
#                               vista ejecutar según la URL solicitada.


# <!--{{}} son para las variables en django--> en html

# La línea path('', views.render, name='home') indica:

# '' → La URL base del sitio (ejemplo: http://tudominio.com/).
# views.mi_vista → Llama a la función mi_vista en views.py cuando un usuario accede a la URL base.
# name='home' → Un nombre opcional para referirse a esta ruta en el código.
