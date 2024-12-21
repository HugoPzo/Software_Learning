# lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
# suma_pares = 0
# suma_impares = 0

# for i in lista_numeros:
#     if (i % 2) == 0:
#         suma_pares += i
#     else:
#         suma_impares += i
        

# lista = list(range(0, 101))
# print(lista)


# lista_elementos = ["a", "b", "c", "d"]

# # Enumerar elementos
# for i in enumerate(lista_elementos):
#     print(i)

# for indice, elemento in enumerate(lista_elementos):
#     print(indice, elemento)

# print("\n")

# for indice, elemento in enumerate(range(50,55)):
#     print(indice, elemento)


# lista_tuples = list(enumerate(lista_elementos))
# print(lista_tuples)


# from random import *


# aleatorio = uniform(1, 5)
# print(aleatorio)

# aleatorio = random()
# print(aleatorio)


# pies = [10, 20, 30, 40, 50]
# metros = [i / 3.281 for i in pies]

# print(metros)


# valores = [1, 2, 3, 4, 5, 6, 9.5]

# valores_pares = [valor for valor in valores if valor % 2 == 0]

# print(valores_pares)

# temperatura_fahrenheit = [32, 212, 275]

# grados_celsius = [(grados_celsius-32)*(5/9) for grados_celsius in temperatura_fahrenheit]

# print(grados_celsius)


# serie = "N-02"

# match serie:
#     case "N-01":
#         print("Samsung")
#     case "N-02":
#         print("Nokia")
#     case "N-03":
#         print("Motorola")
#     case _:
#         print("No existe el producto.")

    
cliente = {"nombre": "Federico", 
           "edad": 45, 
           "ocupacion": "instructor"}

pelicula = {"titulo": "Matrix",
            "ficha_tecnica": {"protagonista": "keanu reeves",
                              "director": "Lana & Lilly Wachowski"}}

elementos = [cliente, pelicula, "libro"]

for elemento in elementos:
    match elemento:
        case {"nombre": nombre,
              "edad": edad,
              "ocupacion": ocupacion}:
            print(f"{nombre} es un cliente")
            print(nombre, edad, ocupacion)
        case {"titulo": titulo,
              "ficha_tecnica": {"protagonista": protagonista,
                                "director": director}}:
            print("Es una pelicula")
            print(titulo,protagonista,":",director)
        case _:
            print("Es un libro")

