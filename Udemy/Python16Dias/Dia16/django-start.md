```markdown
# 📌 Guía para Iniciar un Proyecto Django

## 1️⃣ Instalar Django
Si aún no tienes Django instalado, primero crea un entorno virtual y luego instálalo:

```sh
python -m venv venv  # Crear entorno virtual
source venv/bin/activate  # Activar en macOS/Linux
venv\Scripts\activate  # Activar en Windows

pip install django  # Instalar Django
```

Para verificar la instalación:
```sh
django-admin --version
```

---

## 2️⃣ Crear un Proyecto Django
Ejecuta el siguiente comando para crear un nuevo proyecto:

```sh
django-admin startproject mi_proyecto
```

Esto generará una estructura como esta:

```
mi_proyecto/
│── manage.py
│── mi_proyecto/
    │── __init__.py
    │── settings.py
    │── urls.py
    │── asgi.py
    │── wsgi.py
```

---

## 3️⃣ Ejecutar el Servidor de Desarrollo
Navega al directorio del proyecto y ejecuta el servidor:

```sh
cd mi_proyecto
python manage.py runserver
```

Esto iniciará el servidor en `http://127.0.0.1:8000/`.

---

## 4️⃣ Crear una Aplicación dentro del Proyecto
Django organiza el código en aplicaciones dentro del proyecto:

```sh
python manage.py startapp mi_app
```

Esto creará una carpeta `mi_app/` con la estructura:

```
mi_app/
│── migrations/
│── __init__.py
│── admin.py
│── apps.py
│── models.py
│── tests.py
│── views.py
```

Agrega la aplicación a `settings.py`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    ...
    'mi_app',
]
```

---

## 5️⃣ Crear un Modelo (Base de Datos)
En `models.py`, define un modelo:

```python
from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()

    def __str__(self):
        return self.nombre
```

Aplica la migración:

```sh
python manage.py makemigrations
python manage.py migrate
```

---

## 6️⃣ Crear un Superusuario para el Panel de Administración
```sh
python manage.py createsuperuser
```
Accede a `http://127.0.0.1:8000/admin/` con las credenciales creadas.

---

## 7️⃣ Crear una Vista y una URL
En `views.py` de `mi_app`:

```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("¡Hola, Django!")
```

En `urls.py` del proyecto:

```python
from django.urls import path
from mi_app.views import home

urlpatterns = [
    path('', home),
]
```

---

Ahora, si abres `http://127.0.0.1:8000/`, verás **"¡Hola, Django!"** 🎉.

Si necesitas más detalles o quieres agregar más funcionalidades, dime qué necesitas. 🚀
```

