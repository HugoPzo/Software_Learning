
## COMO FUNCIONAN LOS OBJETOS

# def mayuscula(texto):
#     print(texto.upper())

# def minuscula(texto):
#     print(texto.lower())


# mi_funcion = mayuscula


# ---------------------------- #


# mi_funcion("Hola")

# def mayuscula(texto):
#     print(texto.upper())

# def minuscula(texto):
#     print(texto.lower())


# def una_funcion(funcion):
#     return funcion


# una_funcion(mayuscula("Hola"))


# ---------------------------- #


## EN PYTHON SE PUEDEN DEFINIR FUNCIONES DENTRO DE OTRAS FUNCIONES


# def mi_funcion(tipo):
    
#     def mayuscula(texto):
#         print(texto.upper())

#     def minuscula(texto):
#         print(texto.lower())


#     if tipo == "may":
#         return mayuscula
    
#     elif tipo == "min":
#         return minuscula
    


# mayus = mi_funcion("may")
# mayus("hola")
# minus = mi_funcion("min")
# minus("HOLA")


# ---------------------------- #
## DECORADOR
## LOS DECORADORES AÑADEN FUNCIONALIDAD A LAS FUNCIONES

# UN DECORADOR ENVUELVE A TODA LA FUNCION PASADA 
def decorar_saludo(funcion):

    def otra_funcion(palabra):
        print("HOLA")
        funcion(palabra)
        print("ADIOS")

    # Retorna esta funcion en lugar de la original
    return otra_funcion


# @decorar_saludo
# Envuelve la funcion 'mayuscula' dentro de la funcion 'decorar_saludo'
def mayuscula(texto):
        print(texto.upper())

@decorar_saludo
def minuscula(texto):
    print(texto.lower())


mayuscula("python") # PYTHON
print("\n")


minuscula("PYTHON") # HOLA \n python /n ADIOS
print("\n")


# Funcion sin decorador
mayuscula_decorada = decorar_saludo(mayuscula)
mayuscula_decorada("hugo")

print("\n")

minuscula_decorada = decorar_saludo(minuscula)
minuscula_decorada("HUGO")
