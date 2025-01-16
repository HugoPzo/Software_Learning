import requests
import bs4
import re


base_url = "https://www.elpalaciodehierro.com/hombre/ropa/?start={}&sz=52"

for num_pag in range(0,104,52):
    url = base_url.format(num_pag)
    result = requests.get(url)
    soup = bs4.BeautifulSoup(result.text, 'lxml')
    products = soup.select(".l-plp-grid_item.m-product")

    for product in products:
        product_info = product.select(".b-product")[0].attrs["data-analytics"]

        name_pattern = r'("name":"\D{1,},")'
        brand_pattern = r'("brand":"\D{1,},")'
        price_pattern = r'("price":\d*)'

        print(re.search(name_pattern, product_info))
        print(re.search(brand_pattern, product_info))
        print(re.search(price_pattern, product_info))
        print("\n")

        

        