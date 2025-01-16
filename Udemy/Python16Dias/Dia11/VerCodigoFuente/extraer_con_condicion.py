import bs4
import requests

# URL SIN NUMERO DE PAGINA
url_base = "https://books.toscrape.com/catalogue/page-{}.html"

# LISTA DE TITULOS CON 4 O 5 ESTRELLAS
titulos_rating_alto = []

# ITERAR PAGINAS

for pagina in range(1, 6):
    # VISITAMOS CADA URL
    url = url_base.format(pagina)
    result = requests.get(url)
    soup = bs4.BeautifulSoup(result.text, 'lxml')

    # SELECCIONAMOS TODOS LOS LIBROS
    libros = soup.select(".product_pod")

    # ITERAR LIBROS
    for libro in libros:
        # CHEQUEAR QUE TENGAN 4 O 5 ESTRELLAS
        if len(libro.select(".star-rating.Four")) != 0 or len(libro.select(".star-rating.Five")) != 0:
            
            # GUARDAR TITULO DEL LIBRO
            titulo_libro = libro.select('a')[1]['title']

            # AGREGAR LIBRO A LA LISTA
            titulos_rating_alto.append(titulo_libro)


# VER LIBROS DE 4 U 5 ESTRELLAS EN CONSOLA
for titulo in titulos_rating_alto:
    print(titulo)


