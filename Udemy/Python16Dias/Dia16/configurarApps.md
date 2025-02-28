# 📌 Crear una Aplicación en Django - Paso a Paso

## 1⃣ Crear un Proyecto en Django
Si aún no tienes un proyecto de Django, primero debes crearlo.

```bash
django-admin startproject mi_proyecto
cd mi_proyecto
```

Esto generará la siguiente estructura:

```
mi_proyecto/
│-- manage.py
│-- mi_proyecto/
│   │-- __init__.py
│   │-- settings.py
│   │-- urls.py
│   │-- asgi.py
│   │-- wsgi.py
```

---

## 2⃣ Crear una Aplicación en Django
Dentro del proyecto, crea una nueva aplicación con:

```bash
python manage.py startapp mi_app
```

Esto creará una nueva carpeta llamada `mi_app` con la siguiente estructura:

```
mi_app/
│-- __init__.py
│-- admin.py
│-- apps.py
│-- models.py
│-- tests.py
│-- views.py
│-- migrations/
│   └── __init__.py
```

---

## 3⃣ Registrar la Aplicación en `settings.py`
Para que Django reconozca la nueva aplicación, agrégala en `INSTALLED_APPS` dentro del archivo `settings.py`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mi_app',  # Agregar aquí la app creada
]
```

---

## 4⃣ Crear una Vista en `views.py`
El archivo `views.py` es donde definimos las funciones que manejarán las solicitudes HTTP.

Edita `mi_app/views.py` y agrega lo siguiente:

```python
from django.http import HttpResponse

def inicio(request):
    return HttpResponse("¡Hola, este es mi primer app en Django!")
```

📌 **Explicación**:
- `from django.http import HttpResponse`: Importamos `HttpResponse`, que permite devolver una respuesta en texto.
- `def inicio(request)`: Creamos una función llamada `inicio` que recibe una petición HTTP.
- `return HttpResponse("¡Hola, este es mi primer app en Django!")`: La función responde con un mensaje en texto plano.

---

## 5⃣ Configurar una URL para la Vista
Para que esta vista sea accesible desde una URL, necesitamos configurar las rutas.

1⃣ **Crea un archivo `mi_app/urls.py`** (si no existe) y agrega:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
]
```

📌 **Explicación**:
- `path('', views.inicio, name='inicio')`: Define la URL base (`''` significa que es la página principal de la app).
- `views.inicio`: Llama a la función `inicio` definida en `views.py`.

2⃣ **Ahora, edita `urls.py` del proyecto** y agrega:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mi_app/', include('mi_app.urls')),  # Vincular la app con el proyecto
]
```

📌 **Explicación**:
- `path('mi_app/', include('mi_app.urls'))`: Todas las URLs que empiecen con `mi_app/` serán manejadas por `mi_app/urls.py`.

---

## 6⃣ Ejecutar el Servidor y Probar
Ejecuta el servidor de desarrollo con:

```bash
python manage.py runserver
```

Luego, abre un navegador y visita:  
📍 `http://127.0.0.1:8000/mi_app/`  

Deberías ver el mensaje:  
**"¡Hola, este es mi primer app en Django!"** 🎉

---

## 7⃣ Crear y Aplicar Migraciones (Opcional)
Si trabajas con bases de datos, debes definir modelos en `models.py` y ejecutar:

```bash
python manage.py makemigrations
python manage.py migrate
```

📌 **Explicación**:
- `makemigrations`: Crea archivos de migración con los cambios en la base de datos.
- `migrate`: Aplica los cambios a la base de datos.

---

## 🎯 ¡Listo! 🚀
Has creado y registrado una aplicación en Django correctamente. Ahora puedes seguir desarrollando tu proyecto.

---

### 📌 Siguientes Pasos
✅ Crear modelos en `models.py`  
✅ Usar plantillas HTML con `render()`  
✅ Conectar Django con una base de datos  

---

¡Espero que esta guía te ayude! ¿Quieres profundizar en algún paso? 😃