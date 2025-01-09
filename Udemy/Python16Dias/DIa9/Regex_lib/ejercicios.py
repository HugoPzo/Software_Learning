import re
# VERIFICAR CORREO --------------------------------------------



# # Regex Email
# #   ^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$

# def verificar_email(email):
#     patron = r"(\w+)@(\w+)\.(\w+)" # r'@\w+\.com'

#     resultado = re.search(patron, email)
#     print(resultado)

#     if resultado:
#         return print("Ok")
#     else:
#         return print("La dirección de email es incorrecta")
    


# verificar_email("usuario@hostcom")


# VERIFICAR SALUDO --------------------------------------------

# def verificar_saludo(frase):
#     patron = r"^Hola"
#     resulado = re.search(patron, frase)

#     print(resulado)

#     if resulado:
#         return print("Ok")
#     else:
#         return print("No has saludado")
    

# verificar_saludo("Hola, como estas")
# verificar_saludo("fsdf, como estas")

# VERIFICAR CODIGO POSTAL --------------------------------------------


def verificar_cp(cp):
    patron = r"\w{2}\d{4}"
    resultado = re.search(patron, cp)

    if resultado:
        return print("Ok")
    else:
        return print("El código postal ingresado no es correcto")
