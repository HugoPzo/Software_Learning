# # Funcion Normal (Produce el 4)
# def mi_funcion():
#     return 4

# # Generador (Genera el 4)
# def mi_generador():
#     yield 4


# print(mi_funcion()) # 4

# print(mi_generador()) # <generator object mi_generador at 0x0000024D5A6789E0>

# # COMO PRODUCIR CON EL GENERADOR
# # ACCEDEMOS AL DATO QUE BUSCAMOS
# g = mi_generador()
# print(next(g)) # 4


# ------------------------------ #

# def mi_funcion():
#     lista = [i**2 for i in range(1, 10)]
#     return lista

# def mi_generador():
#     for i in range(1, 10):
#         yield i ** 2


# print(mi_funcion()) # [1, 4, 9, 16, 25, 36, 49, 64, 81]
# print(mi_generador()) # <generator object mi_generador at 0x000002E7ABD0DEE0>

# # Debemos crear una variable de la funcion
# g = mi_generador()
# # Accede a los datos conforme el codigo lo necesita
# print(next(g)) # 1
# print(next(g)) # 4
# print(next(g)) # 9
# print(next(g)) # 16
#             # 25 aun no existe 


# ------------------------------ #

# A DIFERENCIA DE LAS FUNCIONES NORMALES CON 'return', EN UN GENERADOR PODEMOS USAR 'yields' todo el tiempo - No interrumpe el sistema
def mi_generador():
    x = 1
    yield x # Primer next()
    
    x += 1
    yield x # Segundo next()

    x += 1
    yield x # Tercer next()


g = mi_generador()

print(next(g))  # 1

# Se puede colocar codigo entre 'next'
print("Espacio de Generador")

print(next(g))  # 2
print(next(g))  # 3
