lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0

for i in lista_numeros:
    if (i % 2) == 0:
        suma_pares += i
    else:
        suma_impares += i
        

lista = list(range(0, 101))
print(lista)


lista_elementos = ["a", "b", "c", "d"]

# Enumerar elementos
for i in enumerate(lista_elementos):
    print(i)

for indice, elemento in enumerate(lista_elementos):
    print(indice, elemento)

print("\n")

for indice, elemento in enumerate(range(50,55)):
    print(indice, elemento)


lista_tuples = list(enumerate(lista_elementos))
print(lista_tuples)