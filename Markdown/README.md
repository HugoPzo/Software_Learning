# Aprendiendo _Markdown_

-> Ejemplo Estructura
** Estructura

NO USAR (-) EN HEADERS

# --- Parrafos ---

Parrafo - Se divide por 'Enter'

Lorem ipsum dolor sit amet consectetur adipisicing elit. Minus consequuntur accusamus sequi, temporibus aliquid ad, nihil sint pariatur veritatis itaque vitae. Iure ea accusamus repellendus numquam asperiores deserunt consequuntur nihil.

---
# ---- Encabezados ----
** \# Encabezado

Se deben separar por un espacio

# Encabezado 1
## Encabezado 2
### Encabezado 3
#### Encabezado 4
##### Encabezado 5 
###### Encabezado 6 

---
# - Negritas & Cursiva -
_Cursiva_ -> _ Texto _

**NEGRITA** -> ** TEXTO **

---
# --- Enlaces ---
** [ NombreURL(alt) ] ( Enlace )


[YouTube](https://www.youtube.com/)

[FesAragon](https://www.aragon.unam.mx/fes-aragon/#!/inicio)


### Enlaces a Headers
** [ NombreHeader ] ( #NombreHeader )
[Header1](#encabezado-1)

### Enlace a Gmail
email.gmail@gmail.com

---
# -- Imagenes & GIF --
** ![ NombreIMG(alt) ] ( Enlace )

![ImagenDelBBicho](https://imgs.search.brave.com/ADKN3lKGHDS_tSG1g50NRTPgQiIL914DoynqYWmH0oM/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly93d3cu/YWxqYXplZXJhLmNv/bS93cC1jb250ZW50/L3VwbG9hZHMvMjAy/Mi8wOC9BUDE5MTYw/NzU0MTc0OTYwLmpw/Zz9maXQ9MTE3MCw3/ODAmcXVhbGl0eT04/MA)

![Siuuu](./img/bicho.webp)

![Animacion](https://imgs.search.brave.com/dFKpR3hXF66jXYBJfeOy-rYHBnziDOhzJhAi9G7XtHE/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YTIuZ2lwaHkuY29t/L21lZGlhL0Y0aHBy/dDNKdlMxUzgvMjAw/LmdpZj9jaWQ9Nzkw/Yjc2MTEydTJmdzM4/eXgza3ZiNWQ0Z2hk/b2JwbmM4Z2I3cnl0/enI2ZzJwdGQ3JmVw/PXYxX2dpZnNfc2Vh/cmNoJnJpZD0yMDAu/Z2lmJmN0PWc.gif " GIF ")

---
# -- Divisiones -- 

Division de Contenido - Semanticamente se habla de otro tema

( --- ) -> Tres lineas juntas

---
---


---
# -- Listas --

### Ordenadas

( 1. )

1. Primero
2. Segundo
3. Tercero
4. Cuarto

### Desordenadas

( *, - )

* Uno
- Dos
* Tres
- Cuarto


### Sublista

- Primavera
    - Abril
    -Mayo
- Verano
    - Julio
    - Agosto
- Otoño
    - Octubre
        - Cumpleaños 🎂
- Invierno
    - Enero

---
# - Citas -

( > Cita)

### Cita en linea

> Siempre tienes opcion de no tener opinion - Marco Aurelio

### Cita en bloque

>
> Todo lo que escuchamos es una opinion, no un hecho.
>
> Todo lo que vemos es una perspectiva, no la verdad.
>
> Marco Aurelio
>

---
# - Tablas -

( | Texto | Texto | Texto | ) -> Encabezados

( | --- | --- | --- | ) -> Fila  

( | Fila1 | Fila1| | Fila1 )


| Nombre | Edad | Correo |
| --- | --- | --- |
| Hugo | 11 | hugo@gmail.com |
| Mautie | 12 | mau@gmail.com |
| San | 83 | san@gmail.com |

---
# - CODIGO -
(   Codigo  (``) -> Entre comillas gruesas )

### En linea

Lorem ipsum dolor sit amet consectetur adipisicing elit. Minus consequuntur accusamus sequi, `import tkinter` ad, nihil sint pariatur veritatis itaque vitae. Iure ea accusamus repellendus numquam asperiores deserunt consequuntur nihil.

### En bloque

( `` ```lenguaje_programacion - > Entre 3 veces comillas gruesas ) Se pone a un lado de las comillas el lenguaje de programacion, para (funciones, objetos, librerias, etc...)

```py
from tkinter import *

window = Tk()

print("Hola")

window.mainloop()
```
---
### Markdown Identifica HTML
<form>
    <label>
        Email
        <input type="email" placeholder="email@gmail.com">
    </label>
</form>

# - Comentario -

( <!- - Comentario - -> )

<!-- Esto es un comentario -->
<!-- Esto es otro comentario -->

# - Escape de Caracteres -

Ignorar el uso de caracteres Markdown ( \ )

\*\*Cursiva\*\*

\_Cursiva\_

# - Badges -

Badges en Google 

![Wikipedia](https://img.shields.io/badge/Wikipedia-%23000000.svg?style=for-the-badge&logo=wikipedia&logoColor=white)
	![Codewars](https://img.shields.io/badge/Codewars-B1361E?style=for-the-badge&logo=codewars&logoColor=grey)

#### Badges Dinamicas

![GitHub followers](https://img.shields.io/github/followers/HugoPzo)

# - Emojis -

https://gist.github.com/rxaviers/7360908


:man:
:kissing_closed_eyes:

# - Videos - 

<!-- Maxima Resolucion -->
<!-- [![Desripcion Video](https://img.youtube.com/vi/idVideo(v=~~~)/maxresdefault.jpg)](https://youtu.be/YesLIU6TkI4) -->

<!-- Minima Resolucion -->
<!-- [![Desripcion Video](https://img.youtube.com/vi/idVideo(v=~~~)/hqdefault.jpg)](https://youtu.be/YesLIU6TkI4) -->

[![Desripcion Video](https://img.youtube.com/vi/YesLIU6TkI4/maxresdefault.jpg)](https://youtu.be/YesLIU6TkI4)

# Hacks de Texto

<ins> Texto Subrayado </ins>

<center> Texto Alineado al Centro </center>

<p style="color:lightgreen"> Texto de Color </p>

# Diagramas de Flujo

<!-- Programa Tutos -->