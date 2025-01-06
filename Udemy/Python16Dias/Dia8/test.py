# Paquete
from Mi_Paquete import suma_resta
# Sub Paquete
from Mi_Paquete.Paquete_subpaquete import saludo

suma_resta.suma(5, 4, 4, 1, 7)

suma_resta.resta(4, 1)

saludo.saludar()


try:
    # Codigo a probar
    pass

except: # except ERROR - Exception(any error)
    # Codigo a ejecutar si hay un error
    pass

else: 
    # Codigo que se ejecuta si no hay un error
    pass

finally:
    # Codigo que se ejecuta de cualquier forma 
    pass