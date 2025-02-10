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

        result_name = re.search(name_pattern, product_info)
        result_brand = re.search(brand_pattern, product_info)
        result_price = re.search(price_pattern, product_info)

        if result_name and result_brand and result_price:
            print(result_name.group())
            print(result_brand.group())
            print(result_price.group())
            
        
        print("\n")

        

        