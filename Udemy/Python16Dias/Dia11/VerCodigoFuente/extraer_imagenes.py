import bs4 # beautiful soup 4
import requests 


URL = "https://www.elpalaciodehierro.com/"

result = requests.get(URL)
result_text = result.text


bs4_result = bs4.BeautifulSoup(result_text, 'lxml')

# imagenes = bs4_result.select("img")
# for img in imagenes:
#     print(img)

imagenes_select = bs4_result.select(".b-content_tile_1-image")
url_imagenes = []
for img in imagenes_select:
    url_imagenes.append(img.attrs['data-src'])

# DESCARGAR IMAGENES 

imagen_primera = requests.get(url_imagenes[0])
# print(imagen_primera) # <Response [200]>
# print(imagen_primera.content) # IMAGEN EN CODIGO BINARIO

# COMVERTIRLO A IMAGEN (EXTRAERLO)
#    open(nombre_a_usar.formato, "wb" -> write binary)
with open("imagen_primera.png", "wb") as file:
    file.write(imagen_primera.content) # SE EXTRAE LA IMAGEN 
    file.close()