Aquí tienes una guía paso a paso en **Markdown** sobre cómo crear un modelo en **Django**.  

```markdown
# 📌 Guía para Crear un Modelo en Django

## 📖 Introducción
Django utiliza modelos para definir la estructura de la base de datos en código Python, lo que facilita su manipulación a través del ORM (Object-Relational Mapping).

---

## 🛠️ Paso 1: Crear una Aplicación en Django
Si aún no tienes una aplicación dentro de tu proyecto, créala con:

```bash
python manage.py startapp mi_app
```

Esto generará una carpeta llamada `mi_app` con la estructura básica.

---

## 🏗️ Paso 2: Definir el Modelo
Edita el archivo `models.py` dentro de `mi_app` y agrega lo siguiente:

```python
from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    email = models.EmailField(unique=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
```

📌 **Explicación de los campos:**
- `CharField`: Campo de texto con longitud máxima de 100 caracteres.
- `IntegerField`: Campo para almacenar números enteros.
- `EmailField`: Campo exclusivo para correos electrónicos.
- `DateTimeField(auto_now_add=True)`: Guarda la fecha y hora de creación.

---

## 🔗 Paso 3: Registrar el Modelo en el Administrador de Django
Abre `admin.py` en `mi_app` y agrégalo:

```python
from django.contrib import admin
from .models import Persona

admin.site.register(Persona)
```

Esto permitirá gestionar el modelo desde el panel de administración.

---

## 🔄 Paso 4: Crear y Aplicar Migraciones
Ejecuta los siguientes comandos para reflejar los cambios en la base de datos:

```bash
python manage.py makemigrations
python manage.py migrate
```

Estos comandos generan y aplican las migraciones necesarias en la base de datos.

---

## 🚀 Paso 5: Probar en la Consola de Django
Puedes probar el modelo interactuando con él desde la consola de Django:

```bash
python manage.py shell
```

Dentro de la consola, prueba lo siguiente:

```python
from mi_app.models import Persona

# Crear una nueva persona
persona = Persona(nombre="Juan Pérez", edad=30, email="juan@example.com")
persona.save()

# Consultar todas las personas
Personas = Persona.objects.all()
print(Personas)
```

---

## 🎨 Paso 6: Personalizar el Modelo (Opcional)
Puedes agregar métodos personalizados dentro del modelo:

```python
class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    email = models.EmailField(unique=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def es_mayor_de_edad(self):
        return self.edad >= 18
```

Este método `es_mayor_de_edad()` permite verificar si la persona tiene al menos 18 años.

---

## 🎯 Conclusión
Siguiendo estos pasos, ya tienes un modelo funcional en Django. Puedes seguir expandiendo el modelo agregando más campos, relaciones con otras tablas o validaciones adicionales.

¡Feliz programación! 🚀
```

Este contenido es completamente formateado en **Markdown**, listo para ser usado en documentación o en plataformas compatibles como **GitHub** o **Notion**. 🚀


### 📌 **Explicación de la Clase `Meta` en Django**

En Django, la clase interna **`Meta`** dentro de un modelo se usa para definir opciones adicionales sobre el comportamiento del modelo, como su ordenación, restricciones o nombre en la base de datos.

---

### 📖 **Clase `Meta` en el Modelo `Tarea`**
Dentro del modelo que compartiste:

```python
class Meta:
    # Manera de ordenacion de las tareas en nuestra tabla
    ordering = ['completo']  # Una vez completas se mandan al final de la lista
```

**🔍 ¿Qué hace `ordering = ['completo']`?**
- Ordena los registros en función del campo `completo`.
- Como `completo` es un `BooleanField` (`True` o `False`), Django los ordenará colocando primero los valores `False` (Tareas **incompletas**) y después los `True` (Tareas **completadas**).
- Esto significa que las tareas sin completar aparecerán **primero** en la lista.

📌 **Si quisieras ordenar en orden inverso (mostrando primero las tareas completas), podrías hacer:**
```python
ordering = ['-completo']  # El signo '-' indica orden descendente
```

---

### 📜 **Otras Opciones Comunes en `Meta`**
Django permite definir varias opciones en `Meta`, por ejemplo:

#### 🔹 **1. Cambiar el Nombre de la Tabla en la Base de Datos**
```python
class Meta:
    db_table = 'mi_tarea'
```
- Esto cambiaría el nombre de la tabla en la base de datos de `app_tarea` (nombre por defecto) a `mi_tarea`.

#### 🔹 **2. Especificar un Nombre para Mostrar en el Admin**
```python
class Meta:
    verbose_name = "Tarea"
    verbose_name_plural = "Tareas"
```
- `verbose_name`: Nombre singular para la entidad.
- `verbose_name_plural`: Nombre en plural para la entidad.

#### 🔹 **3. Restringir Duplicados con `unique_together`**
```python
class Meta:
    unique_together = ['usuario', 'titulo']
```
- Esto impide que un usuario cree dos tareas con el mismo título.

#### 🔹 **4. Aplicar Permisos Personalizados**
```python
class Meta:
    permissions = [
        ("puede_completar_tarea", "Puede marcar tareas como completas"),
    ]
```
- Permite definir permisos que pueden asignarse a los usuarios.

---

### 🎯 **Conclusión**
La clase `Meta` en Django es una forma poderosa de personalizar el comportamiento de un modelo sin modificar directamente su estructura de base de datos. En tu caso, `ordering = ['completo']` asegura que las tareas incompletas aparezcan primero.

🚀 **¿Quieres agregar más personalización a tu modelo?** ¡Cuéntame y te ayudo!



## Migrar Base de Datos Creada

Creamos el archivo 

`python manage.py makemigrations`

Se crea una carpeta en nuestra app 'migrations' dentro de esta 
viene un archivo que contiene todos los elementos de nuestra tabla creada

Ahora lo migramos a nuestro sitio

`python manage.py migrate`

Se migra nuestra tabla a nuestro sitio

Ahora la registramos dentro del admin de la app

```python 
from models import Tarea

admin.site.register(Modelo)
```