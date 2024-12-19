# Calculadora de Comision

# Proyecto Dia 2

PORCENTAJE_COMISION = 13

user_name = input("Ingresa tu nombre: ")
user_pay = float(input("Ingresa tu salario: "))

comision = round(((user_pay * PORCENTAJE_COMISION) / 100), 2)
total = user_pay + comision


print(f"Hola {user_name}, tu ingreso fue de ${user_pay}, tu comision fue de ${comision} con tu comision quedaria en ${total}")