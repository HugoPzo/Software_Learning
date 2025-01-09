from sys import platform
from os import system

# Check operating system to clean terminal
def check_system_clean():
    # Linux or OS
    if platform == "linux" or platform == "linux2" or platform == "darwin":
        return system("clear")
    # Windows
    elif platform == "win32":
        return system("cls")

check_system_clean()

"""MODULO RELACIONADO CON EL TIEMPO"""

import datetime
import time

# Time -> HORA
print("HORA")
mi_hora = datetime.time(17, 34, 23)
print(mi_hora)# 17:34:23
print(mi_hora.hour)# 17
print(mi_hora.minute)# 34
print(mi_hora.second, "\n")# 23

# Date -> FECHA
print("FECHA")
mi_dia = datetime.date(2025, 10, 17)
print(mi_dia) # 2025-10-17
print(mi_dia.year) # 2025
print(mi_dia.month) # 10
print(mi_dia.day) # 17

print(mi_dia.ctime()) # Fri Oct 17 00:00:00 2025

# Dia Actual - FUNCIONA CON CUALQUIER OBJETO DATETIME.DATE
print(mi_dia.today()) # 2025-01-07
print(mi_dia.today().ctime(), "\n") # Tue Jan  7 00:00:00 2025


# Datetime -> FECHA Y HORA
print("FECHA - HORA")
mi_fecha = datetime.datetime(2025, 5, 15, 22, 10, 15)
print(mi_fecha) # 2025-05-15 22:10:15

print(mi_fecha.astimezone()) # 2025-05-15 22:10:15-06:00

print("Replace Month")
mi_fecha = mi_fecha.replace(day=11)
print(mi_fecha, "\n") # 2025-05-11 22:10:15



# NACIMIENTO - MUERTE
print("NACIMIENTO - MUERTE")
nacimiento = datetime.date(2004, 10, 30)
defuncion = datetime.date(2104, 5, 20)

vida = defuncion - nacimiento
print(vida) # 36361 days, 0:00:00
print(vida.days, "\n") # 36361

# HORAS DESPIERTO
print("HORAS DESPIERTO")
despierto = datetime.datetime(year=2022, month=10, day=10, hour=8, minute=20, second=34)
dormirse = datetime.datetime(year=2022, month=10, day=10, hour=23, minute=21, second=53)

horas_despierto = dormirse - despierto
print(horas_despierto) # 15:01:19 - 15 horas con 1 minuto con 19 segundos
print(horas_despierto.seconds, "\n") # 54079 segundos


# MI FECHA Y HORA ACTUAL

# PACKAGE TIME
mi_fecha_hora = time.ctime()
print(mi_fecha_hora, "\n") # Hora y Fecha Actual

mis_minutos = time.strftime("%M") 
print(mis_minutos, "\n") # Minutos Actual

# PACKAGE DATETIME
current_time = datetime.datetime.now()
print(current_time) # HORA Y FECHA ACTUAL

print(current_time.minute) # Minutos Actual
