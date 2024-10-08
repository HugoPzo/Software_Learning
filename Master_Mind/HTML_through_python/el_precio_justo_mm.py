import random
from requests_html import HTMLSession
from speak_and_listen import speak, hear_me

def hear_price_and_get_number():
    # Si el usurio proporciona otra inf. no deseado, repetimos
    while True:
        try:
            price = hear_me()
            # Remplazamos los posibles 'strings' con strings deseasdos
            price.replace(" $", "").replace(",", ".").replace(" con", ".")
            final_price = float(price)
            return final_price
        except ValueError:
            speak("No te he entendido, repite...")


def get_random_producto_attributes():
    # speak("Bienvenido al precio justo, vamos a intentar adivinar los precios de algunos productos")
    session = HTMLSession()
    main_site = session.get("https://www.elpalaciodehierro.com/")  # Entramos mediante codigo a la pagina web
    categories = main_site.html.find(
        ".b-categories_navigation-link_3")  # Obtenemos en una lista las categorias que existen
    category = random.choice(categories)  # random.choice : Escoge un random en una lista

    # Si queremos descartar una opcion dentro de la lista de categorias usamos...
    # while category.text == "Nombre_a_descartar":
    # category = random.choice(categories)

    product_page = session.get(
        category.attrs["href"])  # Obtenemos el link del producto, el cual se encuentra en el diccionario
    products = product_page.html.find(".m-type_4")
    product = random.choice(products)

    product_link = product.absolute_links  # Cuando solo hay un objeto se llama directamente
    product_brand = product.find(".b-product_tile-brand",
                                 first=True).text  # Filtra el objeto y devuelve el texto del producto
    product_title = product.find(".b-product_tile-name", first=True).text
    product_price = product.find(".b-product_price-value", first=True).text
    product_img = product.find(".h-blend_mode_img lazy entered loaded", first=True)

    # Remplazamos los signo '$' con '' vacio, y ',' con '.'
    final_price = float(product_price.replace("$", "").replace(",", "."))

    return product_title, product_brand, product_link, product_price, product_img

def main():
    # Se inicia el juego, el bot elige un producto al azar y te lo dice
    # Tu debes adivinar el valor del producto
    speak("Binvenido al precio justo, vamos a intentar adivinar los precios de los productos")
    get_random_producto_attributes()
    #Le damos a estas variables un valor
    product_title, product_brand, product_link, product_price = get_random_producto_attributes()
    speak("El nombre del producto es {}, cuanto crees que vale?".format(product_title))
    user_guess = hear_price_and_get_number()
    print(product_title)
    speak("El precio era {}".format(product_price))




if __name__ == "__main__":
    main()


# SEGUIR CON CURSO MASTERMIND -- EL PRECIO JUSTO, HABLAME DEL PRECIO --