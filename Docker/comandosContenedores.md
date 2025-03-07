# Comandos Docker Contenedores

**Como crear un contenedor en base a las imagenes que se tienen**

Para crear un contenedor, se necesitan imagenes, en este caso se ocupara mongo

`docker pull mongo`

**Crear un contenedor**

`docker container create <nombre-de-imagen-base>`

o

`docker create <nombre-de-imagen-base>`

Ejemplo

`docker create mongo`

Se nos crea un 'id', el cual es el identificador del container creado, el id lo necesitamos para poder ejecutar nuestro contenedor

Id ejemplo: 7cd41d8aaac091381be08626635636e5cbae9884b3c487e1144921185b9b05cb

**Correr contenedor**

`docker start <id>`

**Verificar si el contenedor esta corriendo**

`docker ps`

Nos devuelve:

    CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS          PORTS       NAMES

    7cd41d8aaac0   mongo     "docker-entrypoint.s…"   3 minutes ago   Up 29 seconds   27017/tcp   youthful_hugle

- CONTAINER ID: Id del contenedor, se puede usar el 'id' que nos devuelve para los comandos
- Image: En base a que imagen se creo el contenedor
- Commando: Comando que usa el contenedor para ejecutarse
- Created: Hace cuanto se creo el contenedor
- Status: Estado
- Ports: Puerto que el contenedor esta ocupando
- Names: Nombre que tiene el contenedor - se puede usar este nombre para ejecutar o eliminar

**Detener el contenedor**

`docker stop <id-contenedor>`

Ejemplo

`docker stop 7cd41d8aaac0`

**Ver todos los contenedores creados**

    CONTAINER ID   IMAGE                             COMMAND                  CREATED          STATUS                      PORTS                  NAMES
    7cd41d8aaac0   mongo                             "docker-entrypoint.s…"   18 minutes ago   Exited (0) 49 seconds ago                          youthful_hugle
    4bf0c694c625   docker/welcome-to-docker:latest   "/docker-entrypoint.…"   21 hours ago     Exited (255) 21 hours ago   0.0.0.0:8088->80/tcp   welcome-to-docker

**Asignar nombres a nuestros contenedores**

`docker create --name <nombre> <nombre-imagen>`

Ejemplo

`docker create --name monguito mongo`

Ahora se puede ocupar ese nombre para correr el contenedor o eliminar, etc...

`docker start monguito`


## Puertos Docker - Port Mapping


### **¿Qué es el Port Mapping en Docker?**  

El **port mapping** (mapeo de puertos) es el proceso mediante el cual se conecta un puerto del contenedor con un puerto del sistema anfitrión (host). Esto permite acceder a los servicios que corren dentro del contenedor desde el exterior.  

🔹 **Sintaxis básica:**  
```sh
docker run -d -p <puerto_host>:<puerto_contenedor> <imagen>
```
- **`puerto_host`** → Es el puerto del sistema anfitrión (tu computadora o servidor).  
- **`puerto_contenedor`** → Es el puerto dentro del contenedor donde se ejecuta la aplicación.  
- **`imagen`** → Es la imagen de Docker que se usará para crear el contenedor.  

---

### **Ejemplo práctico de Port Mapping**  
Supongamos que tienes una aplicación web que se ejecuta en un contenedor en el puerto `5000` (dentro del contenedor). Para acceder a ella desde tu computadora, necesitas mapear ese puerto a uno en el host, por ejemplo, `8080`:  

```sh
docker run -d -p 8080:5000 mi_aplicacion
```
✅ Esto significa que:  
- La aplicación dentro del contenedor sigue escuchando en `5000`.  
- Pero ahora puedes acceder a ella desde el host en `http://localhost:8080`.  

Si quieres acceder desde otro dispositivo en la misma red, puedes usar la IP del host:  
```sh
http://<IP_DEL_HOST>:8080
```

---

### **Casos de Uso**  
✅ **Ejecutar múltiples contenedores con la misma imagen en diferentes puertos:**  
```sh
docker run -d -p 8081:5000 mi_aplicacion
docker run -d -p 8082:5000 mi_aplicacion
```
- Dos instancias de `mi_aplicacion`, pero una accesible en `8081` y otra en `8082`.  

✅ **Mapear el puerto 80 de un servidor web (Ej: Nginx) al host:**  
```sh
docker run -d -p 80:80 nginx
```
Ahora el servidor web Nginx es accesible en `http://localhost`.  

---

### **Ver los puertos mapeados**  
Para ver qué contenedores están corriendo y qué puertos están mapeados:  
```sh
docker ps
```
Ejemplo de salida:  
```
CONTAINER ID  IMAGE   COMMAND   PORTS                   NAMES
e8b6e7f5a4c2  nginx   ...       0.0.0.0:80->80/tcp      web_server
```
Aquí, `0.0.0.0:80->80/tcp` significa que el puerto `80` del host está redirigido al `80` del contenedor.

---

### **Diferencias con `EXPOSE` en Dockerfile**  
En un `Dockerfile`, puedes usar la instrucción `EXPOSE`, pero esta **no publica el puerto automáticamente**. Solo es una documentación interna para indicar que el contenedor usará ese puerto.  

Ejemplo en `Dockerfile`:  
```dockerfile
EXPOSE 5000
```
Para hacer accesible el puerto, **debes usar `-p` al ejecutar el contenedor**, como vimos antes.  

---

### **Resumen**  
✅ **El Port Mapping permite acceder a servicios dentro de contenedores desde el host**.  
✅ **Se usa el flag `-p` con la sintaxis `-p <puerto_host>:<puerto_contenedor>`**.  
✅ **Se puede mapear diferentes puertos para múltiples instancias del mismo contenedor**.  
✅ **El comando `docker ps` ayuda a verificar los puertos mapeados**.  

---

## Comandos Port Mapping

`docker create -p<numero-puerto-host>:<puerto-contenedor-a-mapear> --name <nombre> <nombre-imagen>`

- p = Publish | Port

Ejemplo

`docker create -p 3000:27017 --name monguito mongo`

**En este caso dejamos a docker escoger el puerto local (No recomendado)**

`docker create -p 27017 --name monguito mongo`

    CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS         PORTS                     NAMES
    f37cd09c7e2e   mongo     "docker-entrypoint.s…"   20 seconds ago   Up 2 seconds   0.0.0.0:3000->27017/tcp   monguito


> PORTS: 0.0.0.0:3000->27017/tcp
> 
> 0.0.0.0 = Maquina local
> 
> 3000 = Puerto de nuesta maquina local lo esta mapeando a
> 
> 27017 = Puerto del contenedor

**Verificar si el servidor se ejecuto de manera correcta**

`docker logs <nombre|id-containe>`

**Seguir escuchando los logs del servidor**

`docker logs --follow <nombre|id-containe>`

---

