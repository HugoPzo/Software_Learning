from django.shortcuts import render
from django.http import HttpResponse

# render se usa para renderizar plantillas HTML, aunque en este código no se está usando.
# HttpResponse permite devolver directamente una respuesta HTTP con contenido de texto.


# Create your views here.

def mi_vista(pedido):
    return HttpResponse("Bienvenido a tu primer pagina web con django")


# def mi_vista(pedido): Se define una función llamada mi_vista, que es una vista en Django.

# Django pasa automáticamente un objeto HttpRequest (en este caso llamado pedido) a la vista.
# pedido contiene detalles de la solicitud del usuario, como la URL, método (GET, POST, etc.), y encabezados.

# return HttpResponse("Bienvenido a tu primer pagina web con django"):
# Devuelve una respuesta HTTP con el mensaje "Bienvenido a tu primer pagina web con django".
# Este mensaje aparecerá como texto plano en el navegador cuando un usuario visite la URL asociada con esta vista.
