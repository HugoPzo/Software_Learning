# CURSO DOCKER

### TEORIA

### Que es un contenedor?

Forma de empaquetar nuestras aplicaciones junto con todas las dependencias que contenga, incluyendo archivos de configuracion:

- Codigo (HTML, JavaScript, Python, etc...)
- Codigo de Aplicacion (Node, PHP, Python, etc...)
- .env (Variables de Entorno)

Los contenedores son portables, facil de compartir. Permite que el desarrollo y el despliegue de las aplicaciones sea mas facil

### Donde se almacenan?

Se almacenan en un:

- Repositorio de contenedores (Similiar a GitHub, pero exclusivo para contenedores)
    
    Existen dos tipos de repositorios:
    
    - **Privados**

    - **Publicos**

        Docker Hub
        
        Dentro del repositorio de Docker Hub 
        - NodeJS
        - Python 
        - MySQL
        - Postgres    
        

### Como se trabaja SIN contenedores?

Todos los involucrados deben instalar las mismas versiones y dependencias que el proyecto ocupa, puede llegar a tardar varias horas o hasta dias.

### Como se trabaja CON contenedores?

Se debe descargar una imagen (basada en linux), la imagen ya tendra sus dependencias o archivos de configuracion que necesita para poder ejecutarse. Corre dentro de la maquina virtual.

### Como se despliega SIN contenedores?

Necesitan el codigo de la aplicacion, indicaciones de como se deben de actualizar las dependencias + archivos de configuracion, sin embargo, es propenso a errores, en caso de que al levantar servidores alguna instalacion salga erroneamente


### Como se despliega CON contenedores?

Todo el equipo se concentra en realizar una 'imagen', la unica dependencia que necesita la 'imagen' para ejecutarse, es el 'runtime de docker'

Se puede automatizar gracias a los 'pipeline' que tienen algunos proveedores de servicio

El despliegue es casi automatico


## Que es una imagen?

Es el empaquetado, el cual contiene: 

- Dependencias
- Codigo
- La imagen es la que se comparte

Con la imagen solo debemos ejecutar un comando para poder correr la aplicacion, ya que esta tiene dentro todas las dependencias corriendo, junto con todas los archivos de configuracion. (Virtualizacion)

> **UN CONTAINER SON CAPAS Y CAPAS DE IMAGENES**

Por lo regular la primera capa es una distribucion de linux (Alpine), sobre esta existen mas capas, hasta la ultima que es nuestra aplicacion. 

> Los containers pesan muy poco


### Diferencia entre una maquina virtual y docker

- VM

    La maquina virtual, virtualiza las aplicaciones y el kernel (windows, linux, macos), las imagenes se hacen muy pesadas


- Docker

    Solo se virtualiza las aplicaciones, ocupa el kernel en el que se esta ejecutando, son mucho mas ligeras, mayor rendimiento


**Tipos de Virtualizacion**

- Para Virtualizacion

    Se trata de entregar la mayor cantidad de acceso del anfitrion a los clientes

- Virtualizacion Parcial

    Solo algunos elementos del hardware se Virtualizacion

- Virtualizacion Completa

    Todos los elementos del hardware del cliente, son virtualizados. Los clientes no acceden al hardware


**Las imagenes de docker se encuentran armadas por capas, si descargamos capas que otras dependencias necesitan, las ocuparan, y no las volveran a descargar**