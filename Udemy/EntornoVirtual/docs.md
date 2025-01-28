# ENTORNOS VIRTUALES


### Ventajas
- Aislamiento de Proyectos
- Portabilidad
- Gestion de Dependencias


### ¿Cómo crearlos?
`python -m venv <nombre_del_entorno>`

Se recomienda que el nombre del entrono sea '_**env**_'

Después del comando se crea una carpeta (entorno) y se debe activar

**UNIX**

`source env/bin/activate`

**WINDOWS**

`env\Scripts\activate`

> 'env' es el nombre por default del entorno

Una vez activado el entorno, ya podremos instalar todas las dependencias requeridas

**PARA DESACTIVAR**

`deactivate`

**PARA CONOCER DEPENDENCIAS Y VERSIONES DEL ENTORNO**

`pip freeze`

> Lista todas las dependencias instaladas en el entorno

**CREAR ARCHIVO DE REQUERIMIENTOS**

`pip freeze > requirements.txt` 

> El listado de las dependencias instaladas se guardara en el archivo 'requirements.txt' (PORTABILIDAD)

**RECREAR EL MISMO ENTORNO**

`pip freeze -r requirements.txt` 

> Instala cada una de las dependencias dentro del archivo