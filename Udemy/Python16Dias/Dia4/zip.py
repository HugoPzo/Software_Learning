nombres = ["Ana", "Hugo", "Valeria"]
edades = [65, 29, 31]
ciudades = ["Mexico", "Lima", "Berlin"] 

nombres_edades = list(zip(nombres, edades))
nombres_edades_ciudad = list(zip(nombres, edades, ciudades))

print(nombres_edades)

print(nombres_edades_ciudad)

for nombre, edad, ciudad in nombres_edades_ciudad:
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")