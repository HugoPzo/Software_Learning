# Conectarse a los contenedores

**Esta no es la forma recomendada de hacer la conexion, sin embargo, se explica cada elemento de docker**

## Buscar en Docker Hub la imagen que se desea configurar, en este caso mongo**

Cuando estemos creando nuestro container, puede que se necesiten parametros de configuracion, estos seran proporcionados por docker, varian dependiendo de la imagen usada

En este caso para mongo, se ocupan dos variables de entorno

      MONGO_INITDB_ROOT_USERNAME, MONGO_INITDB_ROOT_PASSWORD

<br>

1. Comandos para configurar

**Descargar imagen**

`docker pull <imagen>`

**Listamos imagenes**

`docker images`

**Contenedores corriendo**

`docker ps -a`

**Creamos contenedor con parametros o variables de entorno**

`docker create -p 27017:27017 --name monguito -e MONGO_INITDB_ROOT_USERNAME=nico -e MONGO_INITDB_ROOT_PASSWORD=password mongo`

Creamos nuestro contenedor en base a la imagen de mongo

**Contenedores corriendo**

`docker ps -a`

**Arrancamos contenedor**

`docker start monguito`

**Contenedores corriendo**

`docker ps`

**Si ahora corremos nuestra aplicacion, deberia funcionar correctamente con la conexion al servidor en la que se encuentra mongo**

<br>

## Meter aplicacion dentro de un container

52:32