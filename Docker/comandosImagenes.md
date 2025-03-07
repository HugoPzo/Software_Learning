# Comandos Docker Imagenes


## Docker Desktop

**Que incluye docker desktop?**

- Maquina Virtual 
    - Linux
    - Ejecuta containers

- Permite acceder a archivos y red

- Docker Compose, CLI(Command Line Interface)

- Corre Nativamente en windows WSL2(Windows Subsystem for Linux)


## Docker HUB - https://hub.docker.com/

**Incluye todos los contenedores e imagenes que se pueden descargar, junto con sus comandos**

## Comandos Docker

**Para poder ejecutar los comandos, debemos asegurarnos de que 'docker desktop' este corriendo, si no, no se podran ejecutar los comandos**

***Listado de imagenes descargadas***

`docker images`

REPOSITORY                 TAG       IMAGE ID       CREATED         SIZE 

node                       latest    c29271c7f2b4   6 days ago      1.61GB

- REPOSITORY: Nombre de la imagen descargada
- TAG: Etiquetas del repositorio
- IMAGE ID: Identificador unico
- CREATED: Cuando la imagen fue creada
- SIZE: Espacio usado de almacenamiento

***Descargar imagen***

`docker pull <nombre-imagen>`

Se puede descargar nodejs, mariadb, postgres, etc...

Se puede especificar la version deseada, pero en caso de que no sea asi, se descargara la ultima que este disponible, con la etiqueta 'latest'

Una vez que descargamos, se descarga cada una de sus capas

**Descarga por version**

`docker pull node:18`

`docker pull imagen:version`

Descargar version 18 de node - se aplica el mismo formato para todas las imagenes

*Podemos buscar las imagenes dentro de docker hub, ahi se encuentran todas las imagenes disponibles*


***Eliminar Imagenes***

`docker image rm <nombre-imagen>:version`

---

### **Diferencia entre Imagen y Contenedor en Docker**  

📌 **Imagen**  
Una **imagen** en Docker es un paquete inmutable que contiene todo lo necesario para ejecutar una aplicación:  
✅ Sistema operativo base (Ej: Ubuntu, Alpine, Debian, etc.).  
✅ Dependencias y bibliotecas necesarias.  
✅ Código fuente de la aplicación.  
✅ Configuraciones y variables de entorno.  

Las imágenes son **plantillas** para crear contenedores, pero por sí solas no se ejecutan.  

🔹 **Ejemplo de una imagen:**  
Si tienes una aplicación en Python, puedes crear una imagen basada en Python con todas las dependencias necesarias.  

```dockerfile
# Dockerfile para una imagen personalizada
FROM python:3.9   # Imagen base con Python instalado
WORKDIR /app      # Define el directorio de trabajo
COPY . /app       # Copia los archivos de la aplicación
RUN pip install -r requirements.txt  # Instala dependencias
CMD ["python", "app.py"]  # Comando por defecto para ejecutar la app
```
Luego, construyes la imagen con:  
```sh
docker build -t mi_imagen_python .
```
Esta imagen ahora puede usarse para crear múltiples contenedores.  

---

📌 **Contenedor**  
Un **contenedor** es una instancia en ejecución de una imagen. Es decir, cuando ejecutas una imagen, se convierte en un contenedor con un entorno de ejecución aislado.  

🔹 **Ejemplo de un contenedor:**  
Si usas la imagen que creaste antes (`mi_imagen_python`), puedes ejecutar un contenedor con:  
```sh
docker run -d -p 5000:5000 mi_imagen_python
```
✅ Se ejecutará la aplicación dentro del contenedor.  
✅ Puedes tener múltiples contenedores corriendo desde la misma imagen.  
✅ Los contenedores pueden ser iniciados, detenidos y eliminados sin afectar la imagen original.  

Para ver los contenedores en ejecución:  
```sh
docker ps
```
Para detener un contenedor:  
```sh
docker stop <container_id>
```
Para eliminar un contenedor:  
```sh
docker rm <container_id>
```

🔹 **Diferencias Claves**  
| Característica | Imagen | Contenedor |
|--------------|--------|------------|
| ¿Qué es? | Plantilla o blueprint | Ejecución de la imagen |
| ¿Se modifica? | No cambia | Puede cambiar durante la ejecución |
| ¿Se ejecuta? | No, es solo un archivo | Sí, es un proceso en ejecución |
| Persistencia | Permanente en disco | Temporal, puede eliminarse |

En resumen:  
- **Las imágenes son como los moldes de una galleta** 🍪.  
- **Los contenedores son las galletas hechas con ese molde** 🏠.  

¿Te quedó más claro o necesitas un ejemplo más práctico? 🚀


---

Docker es una plataforma que permite crear, distribuir y ejecutar aplicaciones en contenedores. Los contenedores son entornos ligeros y portátiles que incluyen todo lo necesario para ejecutar una aplicación: código, bibliotecas, dependencias y configuraciones.

### **Cómo funciona Docker**  
1. **Imágenes y contenedores**  
   - Una **imagen** de Docker es un paquete que contiene el sistema de archivos y las configuraciones necesarias para ejecutar una aplicación.  
   - Un **contenedor** es una instancia en ejecución de una imagen, que se ejecuta de manera aislada en el sistema operativo.

2. **Docker Engine**  
   - Es el motor que permite crear, ejecutar y gestionar contenedores. Se encarga de la virtualización a nivel de sistema operativo, utilizando el kernel de Linux y características como namespaces y cgroups.

3. **Dockerfile**  
   - Es un archivo que define paso a paso cómo se construye una imagen de Docker. Contiene instrucciones como:
     ```dockerfile
     FROM ubuntu:latest
     RUN apt-get update && apt-get install -y python3
     COPY app.py /app/
     CMD ["python3", "/app/app.py"]
     ```

4. **Docker Hub y Registro de Imágenes**  
   - Docker Hub es un repositorio en línea donde se almacenan imágenes preconstruidas que pueden descargarse y usarse fácilmente.

5. **Gestión de Contenedores**  
   - Para ejecutar un contenedor desde una imagen:  
     ```sh
     docker run -d -p 8080:80 nginx
     ```
   - Para listar contenedores activos:  
     ```sh
     docker ps
     ```
   - Para detener un contenedor:  
     ```sh
     docker stop <container_id>
     ```

6. **Orquestación con Docker Compose y Kubernetes**  
   - **Docker Compose**: Permite definir y ejecutar múltiples contenedores con un solo archivo `docker-compose.yml`.  
   - **Kubernetes**: Administra múltiples contenedores en entornos distribuidos, facilitando el escalado y la disponibilidad.

Docker simplifica la portabilidad, la escalabilidad y la gestión de aplicaciones en cualquier entorno, ya sea desarrollo, pruebas o producción. 🚀