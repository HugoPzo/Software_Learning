# # Generador Infinito  x += 1

# def mi_generador():
#     x = 1
#     yield x
#     while True:
#         x += 1
#         yield x


# generador = mi_generador()

# print(next(generador)) # 1
# print(next(generador)) # 2
# print(next(generador)) # 3
# print(next(generador)) # 4



# ------------------------------ #

# # MULTIPLOS DE '7'

# def mi_generador():
#     x = 7
#     yield x
#     y = 1
#     while True:
#         y += 1
#         yield x * y 


# generador = mi_generador()

# print(next(generador)) # 7
# print(next(generador)) # 14
# print(next(generador)) # 21
# print(next(generador)) # 28


# ------------------------------ #

# RESTADOR DE VIDAS

def mi_generador():
    yield "Te quedan 3 vidas"
    yield "Te quedan 2 vidas"
    yield "Te queda 1 vida"
    yield "Game Over"
    

perder_vida = mi_generador()

print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))