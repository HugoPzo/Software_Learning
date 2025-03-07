# Comando Principal Docker

**Se usa este comando para realizar todas las acciones, docker pull, docker create, docker logs**

**Este es el comando mas importante de docker, si no se encuentra la imagen, la descarga, crea el contenedor e inicia el contenedor**

Corre la aplicacion en primer plano

`docker run <nombre-imagen>`

Corre la aplicacion en segundo plano (dettached)

`docker run -d <nombre-imagen>`

***Union de todos los comandos***

`docker run --name <nombre> -p<pHost>:<pContenedor> -d <nombre-imagen>`

Ejemplo

`docker run --name monguito -p 5000:27017 -d mongo`

**Se ejecuta este comando y automaticamente descarga la imagen si no se ha descargado, posteriormente crea el contenedor con los puertos establecidos y lo inicia en modo dettached**

**Cada que ejecutamos docker run, docker crea un nuevo contenedor cada que sea ejecutado**


    CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                     NAMES
    0c355020195c   mongo     "docker-entrypoint.s…"   7 seconds ago   Up 6 seconds   0.0.0.0:5000->27017/tcp   monguito


---


### **Cómo usar `docker run`** 🚀  

El comando `docker run` se usa para crear y ejecutar contenedores a partir de una imagen.  

### **📌 Sintaxis básica:**  
```sh
docker run [opciones] <imagen> [comando]
```
- **`<imagen>`** → Nombre de la imagen de Docker que quieres ejecutar.  
- **`[opciones]`** → Parámetros opcionales (puertos, volúmenes, variables de entorno, etc.).  
- **`[comando]`** → Comando que se ejecutará dentro del contenedor.  

---

## **1️⃣ Ejecutar un contenedor simple**  
Ejecutar una imagen de `nginx` en segundo plano:  
```sh
docker run -d -p 8080:80 nginx
```
✅ Se ejecuta Nginx en el puerto `80` del contenedor, accesible en `http://localhost:8080`.  
✅ `-d` (detached) hace que el contenedor corra en segundo plano.  

---

## **2️⃣ Ejecutar un contenedor interactivo**  
Si quieres abrir una terminal dentro del contenedor, usa `-it`:  
```sh
docker run -it ubuntu bash
```
✅ Inicia un contenedor basado en Ubuntu.  
✅ `-i` mantiene la sesión activa para recibir comandos.  
✅ `-t` asigna una terminal interactiva.  
✅ `bash` ejecuta la shell dentro del contenedor.  

Para salir sin detener el contenedor: **`Ctrl + P + Q`**  
Para salir y detenerlo: **`exit`**  

---

## **3️⃣ Ejecutar y eliminar el contenedor automáticamente**  
Si solo necesitas ejecutar un contenedor temporalmente:  
```sh
docker run --rm ubuntu echo "Hola Docker"
```
✅ `--rm` elimina automáticamente el contenedor al finalizar.  

---

## **4️⃣ Asignar un nombre al contenedor**  
Si no defines un nombre, Docker asigna uno aleatorio. Puedes definirlo con `--name`:  
```sh
docker run -d --name mi_servidor nginx
```
✅ Ahora puedes referirte a este contenedor por su nombre:  
```sh
docker stop mi_servidor
docker start mi_servidor
```

---

## **5️⃣ Mapear puertos (`-p`)**  
Ejemplo con una aplicación en Flask que corre en el puerto `5000`:  
```sh
docker run -d -p 8080:5000 mi_app_flask
```
✅ Ahora puedes acceder a la app en `http://localhost:8080`.  

---

## **6️⃣ Montar volúmenes (`-v`)**  
Para compartir archivos entre el host y el contenedor:  
```sh
docker run -d -v $(pwd)/data:/app/data mi_app
```
✅ Monta la carpeta `data` del host en `/app/data` dentro del contenedor.  

---

## **7️⃣ Definir variables de entorno (`-e`)**  
Si una aplicación requiere variables de entorno, puedes pasarlas con `-e`:  
```sh
docker run -d -e ENV=produccion -e DB_HOST=localhost mi_app
```
✅ En el contenedor, las variables estarán disponibles como `ENV=produccion` y `DB_HOST=localhost`.  

---

## **8️⃣ Ejecutar en modo restringido (`--memory`, `--cpu`)**  
Si quieres limitar los recursos del contenedor:  
```sh
docker run -d --memory="512m" --cpus="1.0" mi_app
```
✅ **Máximo 512MB de RAM y 1 CPU asignado**.  

---

## **9️⃣ Ver los contenedores activos**  
```sh
docker ps
```
Si quieres ver todos (incluyendo los detenidos):  
```sh
docker ps -a
```

---

## **🔟 Detener y eliminar contenedores**  
Para detener un contenedor en ejecución:  
```sh
docker stop <container_id>
```
Para eliminarlo:  
```sh
docker rm <container_id>
```
Para eliminar todos los contenedores detenidos:  
```sh
docker container prune
```

---

## **📌 Resumen rápido de opciones importantes**  
| Opción                                 | Descripción                                  |
| -------------------------------------- | -------------------------------------------- |
| `-d`                                   | Ejecuta en segundo plano (detached).         |
| `-it`                                  | Modo interactivo con terminal.               |
| `--rm`                                 | Elimina el contenedor cuando termina.        |
| `--name <nombre>`                      | Asigna un nombre al contenedor.              |
| `-p <puerto_host>:<puerto_contenedor>` | Mapea puertos entre el host y el contenedor. |
| `-v <host_path>:<container_path>`      | Monta volúmenes.                             |
| `-e VAR=valor`                         | Define variables de entorno.                 |
| `--memory`                             | Limita el uso de RAM.                        |
| `--cpus`                               | Limita el uso de CPU.                        |

---

🚀 **Ahora ya sabes cómo usar `docker run`!**  
¿Tienes algún caso específico en mente? 😃