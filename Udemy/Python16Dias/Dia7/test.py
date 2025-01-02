# # Programacion Orientada a Objetos

# class Casa:
#     def __init__(self, color: str, cantidad_pisos: int):
#         self.color = color
#         self.cantidad_pisos = cantidad_pisos
        
        
# casa_blanca = Casa("blanco", 4)
        


class Cubo:
    # Atributo de clase
    caras = 6

    def __init__(self, color):
        # Atributo de instancia
        self.color = color
        
        
cubo_rojo = Cubo("Rojo")