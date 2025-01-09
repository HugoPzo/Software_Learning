
# COUNTER -------------------------------------------------------------------------------------------
from collections import Counter

# # NUMERO DE VECES QUE SE REPITEN LOS NUMEROS
# lista_numeros = [4, 5, 6, 7, 6, 2, 1, 6, 3, 1, 3, 3, 2, 9]
# print(Counter(lista_numeros), "\n") # Counter({6: 3, 3: 3, 2: 2, 1: 2, 4: 1, 5: 1, 7: 1, 9: 1})

# palabra = "hfkjsehfk sdhfks dfksdhfksd kfhsdkf sdfhsdk fsd"
# print(Counter(palabra), "\n") # Counter({'f': 9, 's': 9, 'k': 8, 'd': 8, 'h': 6, ' ': 5, 'j': 1, 'e': 1})

# palabras = "Yo soy ese que esta ahi yo no se nada" 
# print(Counter(palabras.split()), "\n")# Counter({'Yo': 1, 'soy': 1, 'ese': 1, 'que': 1, 'esta': 1, 'ahi': 1, 'yo': 1, 'no': 1, 'se': 1, 'nada': 1})


# # METODOS

# # MAS COMUN
# serie = Counter([1,1,2,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,3,4])
# print(serie.most_common()) # [(1, 8), (2, 6), (3, 6)]
# print(serie.most_common(1)) # [(1, 8)]
# print(serie.most_common(2)) # [(1, 8), (2, 6)]
# print(serie.most_common(3)) # [(1, 8), (2, 6), (3, 6)]

# print(list(serie), "\n") # [1, 2, 3, 4]

# # TOTAL DE ELEMENTOS
# print(serie.total(), "\n") # 21

# # Quitamos elementos del Counter
# serie.subtract([1,1,1,1])
# print(serie, "\n") # Counter({2: 7, 3: 6, 1: 3, 4: 1})

# print(sorted(serie.elements())) # [1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4]



# from collections import Counter
# d ='aabbbcccdeff'
# d = Counter(d)

# # To print Counter value 
# print("d :", d) 

# # To access the values corresponds to each keys of the returned dictionary 
# print("d.values() : ", d.values()) 

# # To get the keys and values both of dictionary
# print("d.items() :", d.items())

# # To get only the keys
# print("d.keys() :", d.keys())

# # To sort the values of dictionary 
# print("sorted(d) :", sorted(d))

# # PRINTS -----
# # d : Counter({'b': 3, 'c': 3, 'a': 2, 'f': 2, 'e': 1, 'd': 1})
# # d.values() :  dict_values([2, 3, 3, 2, 1, 1])
# # d.items() : dict_items([('a', 2), ('b', 3), ('c', 3), ('f', 2), ('e', 1), ('d', 1)])
# # d.keys() : dict_keys(['a', 'b', 'c', 'f', 'e', 'd'])
# # sorted(d) : ['a', 'b', 'c', 'd', 'e', 'f']

# -------------------------------------------------------------------------------------------
# # defaultdict 

# from collections import defaultdict

# # SI BUSCAMOS UN ELEMENTO QUE NO EXISTE EN EL DICCIONARIO, DEVUELVE LO QUE PONGAMOS POR DEFAULT

# mi_diccionario = defaultdict(lambda: "NoExiste")

# mi_diccionario[1] = "uno"
# mi_diccionario[2] = "dos"
# mi_diccionario[3] = "tres"

# # ESTE ELEMENTO NO EXISTE
# print(mi_diccionario[4], "\n") # NoExiste

# # ACTUALIZA EL DICCIONARIO 
# print(mi_diccionario, "\n") #defaultdict(<function <lambda> at 0x000001140CB49760>, {1: 'uno', 2: 'dos', 3: 'tres', 4: 'NoExiste'})
# # - SI NO ASIGNAMOS EL VALOR DE UNA LLAVE, SE PONDRA EL ELEMENTO POR DEFAULT
# # defaultdict(<function <lambda> at 0x000001E59BEC96C0>, {(1, 'uno'): 'NoExiste', (2, 'dos'): 'NoExiste', (3, 'tres'): 'NoExiste', 4: 'NoExiste'})

# print(mi_diccionario.values(), "\n") # dict_values(['uno', 'dos', 'tres', 'NoExiste'])

# -------------------------------------------------------------------------------------------
# namedtuple

# from collections import namedtuple

# # Acceso a elementos de tupla de manera tradicional
# mi_tuple = (500, 18, 65)
# print(mi_tuple[1], "\n")

# # Acceder a elementos por nombre - Creamos una tupla nombrada
# Persona = namedtuple("Persona", ["nombre", "altura", "edad"])

# hugo = Persona("hugo", 1.76, 20)

# print(hugo.nombre)
# print(hugo.altura)
# print(hugo.edad)

# -------------------------------------------------------------------------------------------
# deque

# from collections import deque

# # Una cola doblemente terminada o deque (del inglés double ended queue) es una estructura de datos lineal que permite insertar y eliminar elementos por ambos extremos.


# lista_ciudades =deque(["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"])

# lista_ciudades.appendleft("Mexico")
# print(lista_ciudades, "\n")

# lista_ciudades.extendleft(["Mauricio", "Orlando"])
# print(lista_ciudades, "\n")
