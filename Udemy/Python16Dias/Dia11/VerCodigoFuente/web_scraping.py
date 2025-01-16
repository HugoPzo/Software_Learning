import bs4 # beautiful soup 4
import requests 


URL = "https://www.elpalaciodehierro.com/"

# PEDIR LA INFORMACION DE LA PAGINA WEB (URL)
resultado = requests.get(URL)

print(resultado) # <Response [200]>
# print(type(resultado)) # <class 'requests.models.Response'>
# print(resultado.text) # Codigo HTML de la pagina (string)

texto_resultado = resultado.text

# LIBRERIA QUE SIRVE PARA ORGANIZAR EL HTML DE LA PAGINA, NOS PERMITE NAVEGAR POR CADA ETIQUETA

# sopa = bs4.BeautifulSoup(STRING_DE_LA_PAGINA, MOTOR DE BUSQUEDA)
sopa = bs4.BeautifulSoup(texto_resultado, 'lxml')

# print(sopa) # CODIGO HTML ORGANIZADO POR BEAUTIFUL SOUP

# SE DEVUELVE EN UNA LISTA TODAS LAS ETIQUETAS ENCONTRADAS
        # .select("nombre_etiqueta")
print(sopa.select("title")) # [<title>Compra en Línea Ropa, Calzado, Bolsos, Joyería y Belleza | El Palacio de Hierro</title>, <title>card-icon</title>]
print(sopa.select("h1")) # [<h1 class="lg-hide">EL PALACIO DE HIERRO; Rebajas invierno</h1>]
print(sopa.select("h2")) # [<h2 class="smart-title">VIVE EL PALACIO MÁS PERSONAL</h2>, <h2 class="b-banner-csm-p b-banner-csm-h2" style="color:#5E5E5E;">LACOSTE</h2>, <h2 class="b-banner-csm-p b-banner-csm-h2" style="color:#5E5E5E;">Givenchy</h2>, <h2 class="b-banner-csm-p b-banner-csm-h2" style="color:#5E5E5E;">Kurt Geiger</h2>]



# SIN ETIQUETAS

print(sopa.select("h1")[0].get_text()) # EL PALACIO DE HIERRO; Rebajas invierno


# EXTRAER POR CARACTERES ESPECIALES

texto_diseñadores = sopa.select(".b-categories_navigation > .b-categories_navigation-list_1 > .b-categories_navigation-item_1 > .b-categories_navigation-link_1")[1].get_text()
print(f"\nTEXTO DISEÑADORES - {texto_diseñadores}")


