# DJANGO

## Entorno Virtual

Para Django es obligatorio tener un entorno virtual,
el cual pycharm al crear un proyecto ya te lo proporciona
inclusive ya activado. 

Pero si se desea activar es de la siguiente manera:

`python -m venv <nombre-de-entono>`

Esto te creara una carpeta con el nombre de tu entorno
virtual, a continuacion debes activarlo ubicado desde 
tu proyecto principal.

Windows -> `nombre-de-entorno\Scripts\activate`

macOS & Linux -> `source nombre-de-entorno\bin\activate`

Una vez ya activado, ya tendremo habilitada nuestro entorno virtual

Tambien podemos desactivar el entorno virtual con 

`deactivate`

Lo podemos volver a activar con el comando de activacion

---

## Django Configuracion 

Para instalar django dentro de nuestro entorno virtual
escribimos el siguiente comando

`pip install django`

Este nos instalara varias dependencias(modulos), las cuales podemos
revisar con

`pip freeze`

Creamos una subcarpeta dentro del proyecto principal que 
funcionara como fuente (src - source)

`mkdir src`

Nos movemos a la subcarpeta 'src' 
dentro de nuestra carpeta 'src' iniciamos el proyecto
con

`django-admin startproject <nombre-proyecto>`

Dentro de 'src' se crea una carpeta con el <nombre-proyecto>
y un archivo python llamado 'manage.py' el cual es el mas importante ya
que desde ese archivo administramos todo dentro del proyecto

---

## Iniciamos el servidor

Una vez ubicados en nuestra carpeta 'src' podemos correr el servidor con

`python manage.py runserver`

Cuando corramos el servidor, en este caso http://127.0.0.1:8000/, en esta ruta podremos acceder a nuestra pagina

Tambien se creara automaticamente un archivo llamado 'db.sqlite3' 

Se nos pedira migraciones que debemos realizar para que nuestro proyecto trabaje de manera correcta,
las hacemos con este comando

`python manage.py migrate`

Se migran todos los archivos que estaban pendientes por migrar

## Admin

Django crea una ventana de administrador por default, accedemos de esta manera
http://127.0.0.1:8000/admin 

En esta ruta se nos pedira un Username & Password, podemos crear un usuario de la siguiente
manera

`python manage.py createsuperuser`

Nos pedira 

- username
- email
- password (Minimo 8 caracteres)

> Si no son 8 caracteres de password aparecera 
> '"Bypass password validation and create user 
> anyway" significa omitir la validación de 
> contraseña al crear un usuario en Django, 
> permitiendo que el usuario se cree incluso 
> si la contraseña no cumple con los requisitos
> de seguridad establecidos por Django.

Una vez dado cada dato, se crea el usuario exitosamente,
ya podremos acceder al administrador de Django

Dentro del administrador podemos administrar Grupos y Ususarios
por default

---

## Apps - Aplicaciones

> Componentes de un sitio web

Para crear una aplicacion dentro de nuestra carpeta del proyecto

`python manage.py startapp <nombre-de-app>`

Conectar proyecto con una aplicacion

> settings.py - Agregramos

```
INSTALLED_APPS = [
.
.
.
'nombre_app.apps.NombreClase(apps.py)'
]
```

Conectamos las 'urls' de todos los sitios

> Creamos en la carpeta de nuestra app el archivo
> 'urls.py'


En views de nuestra app agregamos - Esto cuando sea llamado, dara una 
respuesta, la cual sera lo que querramos renderizar en la pagina

```python
from django.http import HttpResponse

def render(pedido):
    return  HttpResponse('Lista Pendientes')
```


Dentro del archivo 'urls' de tu app importamos

```python
from django.urls import path
from . import views -> Hace referencia a las vistas de la app

urlpatterns = [
    # Agregamos el path de nuestras vistas y lo renderizamos
    url_patterns = [path('', views.render(), name='home')]
]

```
