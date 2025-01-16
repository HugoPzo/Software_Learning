import requests
import bs4

url_base = "https://books.toscrape.com/catalogue/page-{}.html"
# print(url_base.format(15)) # https://books.toscrape.com/catalogue/page-15.html

lista_urls = []
for num_url in range(1, 11):
    lista_urls.append(url_base.format(num_url))

libro_info = {}
for url in lista_urls:
    result = requests.get(url)
    soup = bs4.BeautifulSoup(result.text, 'lxml')
    libros = soup.select(".product_pod")
    for libro in libros:
        nombres = soup.select(".product_pod>h3>a")
        precios = soup.select(".product_pod>.product_price>.price_color")
        stocks = soup.select(".product_price>.instock.availability")

        # ITERATE IN TWO DIFFERENT LISTS
        for nombre, precio, stock in zip(nombres, precios, stocks):
            libro_info[nombre.attrs['title']] = (precio.getText().replace("Â", ""), stocks[0].get_text().strip())


print(libro_info)


