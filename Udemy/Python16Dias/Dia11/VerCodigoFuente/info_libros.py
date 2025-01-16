import bs4
import requests

url_base = "https://books.toscrape.com/catalogue/page-{}.html"

libro_info = {}
for num_pagina in range(1, 6):
    url = url_base.format(num_pagina)
    
    result = requests.get(url)
    soup = bs4.BeautifulSoup(result.text, 'lxml')

    libros = soup.select(".product_pod")

    for libro in libros:
        
        if len(libro.select(".star-rating.Four")) != 0 or len(libro.select(".star-rating.Five")) != 0:

            titulo = libro.select('h3>a')[0].attrs['title']
            price = libro.select(".product_price>.price_color")[0].get_text().replace("Â", "").strip()
            image = libro.select(".image_container a img")[0].attrs['src']
            stock = libro.select(".product_price>.instock.availability")[0].get_text().strip()

            libro_info[titulo] = {"Price" : price, "Image" : image, "Stock" : stock}


print(libro_info)
