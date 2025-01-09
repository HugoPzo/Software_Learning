# REGEX MODULES
# REGULAR EXPRESIONS

import re

# # String procesado como una expresion regular 'r'

# texto = "Si necesitas ayuda llama al (658)-598-9977 las 24 horas al servicio de ayuda online"

# patron = "ayuda"

# # BUSQUEDA -> re.search(patron, string)
# busqueda = re.search(patron, texto)
# print(busqueda) # <re.Match object; span=(13, 18), match='ayuda'>
# print(busqueda.span()) # (13, 18)
# print(busqueda.start()) # 13
# print(busqueda.end(), "\n") # 18

# # BUSQUEDA DE TODOS 
# busqueda = re.findall(patron, texto)
# print(busqueda) # ['ayuda', 'ayuda']

# # BUSQUEDA EN ITERACION
# for hallazgo in re.finditer(patron, texto):
#     print(hallazgo.span()) # (13, 18) - (71, 76)

# ------------------------------------------------------------------------ #

# texto = "Llama al 658-598-5431 ya mismo"

# # Cadena especial -> Caracteres de un patron
# # patron = r"\d\d\d-\d\d\d-\d\d\d\d"
# # patron = r"\d{3}-\d{3}-\d{4}"
# # patron = re.compile(r"(\d{3})-(\d{3})-(\d{4})")

# resultado = re.search(patron, texto)

# print(resultado) # <re.Match object; span=(9, 21), match='658-598-9977'>
# print(resultado.group()) # 658-598-5431

# # MEDIANTE GRUPOS 're.compile()'
# print(resultado.group(1)) # 658
# print(resultado.group(2)) # 598
# print(resultado.group(3)) # 5431

# ------------------------------------------------------------------------ #
# PEDIR UNA CLAVE ESPECIFICA

# # PEDIMOS QUE EL USUARIO RESPETE EL PATRON 
# clave = input("Clave: ")
# patron = r"\D{1}\w{7}"

# chequear = re.search(patron, clave)

# # SOLO EN CASO DE QUE SE RESPETE, RETORNA EL OBJETO
# print(chequear) # <re.Match object; span=(0, 8), match='D3248185'>

# ------------------------------------------------------------------------ #
# OPERADORES ESPECIALES

texto = "No atendemos los martes por la tarde"

                    # Lunes o Martes
buscar = re.search(r"lunes|martes", texto)

print(buscar, "\n") # <re.Match object; span=(17, 22), match='lunes'>
                    # <re.Match object; span=(17, 23), match='martes'>

# '.' Retorna el caracter anterior
# '....' Retorna los caracteres dependiendo de los puntos
buscar = re.search(r".demos", texto)
print(buscar, "\n") # <re.Match object; span=(6, 12), match='ndemos'>

# '^' Verificar si un patron se encuntra al comienzo del string
buscar = re.search(r"^\D", texto)
print(buscar, "\n") # <re.Match object; span=(0, 1), match='N'>

# '$' Verificar si un patron se encuntra al final del string
buscar = re.search(r"\D$", texto)
print(buscar, "\n") # <re.Match object; span=(22, 23), match='s'>

# '[^]' Excluir todo el patron - En este caso todo los espacios vacios
buscar = re.findall(r"[^\s]", texto)
print(buscar, "\n") # ['N', 'o', 'a', 't', 'e', 'n', 'd', 'e', 'm', 'o', 's', 'l', 'o', 's', 'm', 'a', 'r', 't', 'e', 's', 'p', 'o', 'r', 'l', 'a', 't', 'a', 'r', 'd', 'e']

buscar = re.findall(r"[^\s]+", texto)
print(buscar) # ['No', 'atendemos', 'los', 'martes', 'por', 'la', 'tarde']

