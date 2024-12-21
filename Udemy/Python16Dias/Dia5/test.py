# palabra = ",:_#,,,,,,:::____##Pyt%\on_ _Total,,,,,,::#"

# print(palabra.strip(",:_#%"))


# frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]

# frutas.insert(3, "naranja")

# print(frutas)

# marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}

# marcas_tv = {"Sony", "Philips", "Samsung", "LG"}


# conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)

# print(conjuntos_aislados)


# def saludar():
#     return print("¡Hola mundo!")
    
# saludar()


# # Definir el tipo de dato que debe ser pasado
# def bienvenida(nombre_persona: str):
#     return print(f"¡Bienvenido {nombre_persona}!")

# bienvenida("Federico")



# def invertir_palabra(palabra):
#     return palabra[::-1].upper()



# def chequear_3_cifras(numero):
#     if numero in range(100, 1000):
#         return True
#     else:
#         pass



# def chequear_3_cifras(lista):
#     lista_3_cifras = []
#     for n in lista:
#         if n in range(100, 1000):
#             lista_3_cifras.append(n)
#         else:
#             pass
    
#     return lista_3_cifras


# resultado = chequear_3_cifras([55, 99, 600])
# print(resultado)


# def todos_positivos(lista):
#     return [True if n > 0 else False for n in lista]
            

# lista_numeros  = [43, 53, -5, 23, -325, 235, -23, ]

# print(todos_positivos(lista_numeros))

# def todos_positivos(lista):
#     for n in lista:
#         if n < 0:
#             return False
    
#     return True
    

# lista_numeros  = [43, 53, -5, 23, -325, 235, -23]


# print(todos_positivos(lista_numeros))


# def suma_menores(lista):
#     resultado = 0
#     for n in lista:
#         if n in range(0, 1001):
#             resultado += n
        
#     return resultado



# lista_numeros  = [433, 543, 1035, -5, 23, -325, 235, -23]

# print(suma_menores(lista_numeros))

# def cantidad_pares(lista_numeros): 
#     contador = 0
#     for n in lista_numeros:
#         if n % 2 == 0:
#             contador += 1
            
#     return contador


# lista_numeros = [42, 85, 356, 8221, 4, 563, 54463]


# def reducir_lista(lista):
#     lista_numeros = []
    
#     for i in lista:
#         if i not in lista_numeros:
#             lista_numeros.append(i)
    
#     lista_numeros.remove(max(lista))
#     return lista_numeros
        
            
# def promedio(lista):
    
#     suma = 0
#     for i in lista:
#         suma += i
    
#     promedio = suma / len(lista)
    
#     return promedio


# lista_numeros = [54, 6, 34, 22, 384, 43, 39, 34, 41, 16, 36]

# print(reducir_lista(lista_numeros))




# from random import *

# def lanzar_moneda():
#     lados_moneda = ["Cara", "Cruz"]
#     lado_sorteado = choice(lados_moneda)

#     return lado_sorteado


# def probar_suerte(lado_moneda, lista_numeros):
#     if lado_moneda == "Cara":
#         lista_numeros = []
#         return "La lista se autodestruirá", lista_numeros
#     else:
#         return "La lista fue salvada", lista_numeros


# lista_numeros = [53, 78, 42, 9, 62, 12, 13, 2, 85]


# def suma(*args):
#     return sum(args)

# print(suma(3, 5, 33, 2, 32, 3, 23, 23, 233, 67, 3))


# def suma_cuadrados(*args):
#     total = 0
#     for i in args:
#         total += i**2

#     return total

        
# print(suma_cuadrados(1, 2, 3))


# def suma_absolutos(*args):
#     total = 0
#     for i in args:
#         total += abs(i)

#     return total


# def numeros_persona(nombre, *args):
#     suma_numeros = 0
#     for i in args:
#         suma_numeros += i
    
#     return f"{nombre}, la suma de tus números es {suma_numeros}"



# # def prueba(num1, num2, *args, **kwargs):

# #     print(num1)
# #     print(num2)

# #     for arg in args:
# #         print(arg)


# #     for key, value in kwargs.items():
# #         print(key, value)



# # args = [34, 64, 1, 88, 38, 36]
# # kwargs = {'x': 'uno', 'y': 'dos', 'z': 'tres'}


# # prueba(23, 53, *args, **kwargs)


# def cantidad_atributos(**kwargs):
#     contador = 0
#     for i, j in kwargs.items():
#         contador += 1
#     return contador


# print(cantidad_atributos(34, 563, 21, 432, 623, "holahola"))

# def lista_atributos(**kwargs):
#     lista_valores = []
#     for value in kwargs.values():
#         lista_valores.append(value)

#     return(lista_valores)



# print(lista_atributos(p= 43, r= 233, t= 46))
        

def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}")

    for key, value in kwargs.items():
        print(f"{key}: {value}")