# # Programacion Orientada a Objetos

# class Casa:
#     def __init__(self, color: str, cantidad_pisos: int):
#         self.color = color
#         self.cantidad_pisos = cantidad_pisos
        
        
# casa_blanca = Casa("blanco", 4)


# class Cubo:
#     # Atributo de clase
#     caras = 6

#     def __init__(self, color):
#         # Atributo de instancia
#         self.color = color
        
        
# cubo_rojo = Cubo("Rojo")


# # Tipos de Metodos ------------------------------------------------------

# class Algo:
#     # Constructor
#     def __init__(self):
#         pass

#     # Metodo de Instancia
#     def mi_metodo(self):
#         pass
        
#     # Metodo de 'Clase' -> No estan asociados a las instancias, si no a la clase (No pueden modificar los metodos de instancia, solo los de la clase)
#     @classmethod # Decorador
#     def mi_metodo(cls):
#         pass

#     # Metodos Estaticos -> No aceptan como parametro ni (cls, self), no pueden modificar ni la instancia, ni la clase -> Funciones comunes, que van ligados a la clase
#     @staticmethod
#     def mi_metodo():
#         pass


# # EJEMPLO

# class Pajaro:
    
#     # Atributo de clase
#     alas = True 

#     def __init__(self, color, especie):
#         self.color = color
#         self.especie = especie


#     def piar(self):
#         print("Pio")


#     def volar(self, metros):
#         print(f"El pajaro vuela {metros} metros.")

#         # Metodo Instancia -> Acceder a otros metodos 
#         self.piar()
        
#     # Metodo Instancia -> Puede acceder y modificar atributos
#     def pintar_negro(self):
#         self.color = "negro"
#         print(f"Ahora el pajaro es {self.color}")   


#     # METODOS DE CLASE
#     @classmethod
#     def poner_huevos(cls, cantidad):
#         print(f"El pajaro puso {cantidad} huevos.")
#         # PODEMOS MODIFICAR ATRIBUTOS DE LA CLASE (NO DE INSTANCIA)
#         cls.alas = False
#         print(cls.alas)


#     # METODOS ESTATICOS -> METODOS QUE NO SE MODIFIQUEN
#     @staticmethod
#     def mirar():
#         # NO PODEMOS MODIFICAR ATRIBUTOS DE CLASE, NI DE INSTANCIA+
#         print("El pajaro mira")
        



# piolin = Pajaro("amarillo", "canario")
# piolin.pintar_negro()
# print(piolin.color)

# # Metodos instancia -> Modificar estados de la clase
# piolin.alas = False
# print(piolin.alas)



# # METODO DE CLASE -> NO NECESITAN UNA INSTANCIA PARA PODER EJECUTARSE
# Pajaro.poner_huevos(5)

# # METODOS ESTATICOS 
# Pajaro.mirar()


# # HERENCIA -----------------------------------------

# class Animal:

#     def __init__(self, edad, color):
#         self.edad = edad
#         self.color = color


#     def nacer(self):
#         print("El animal ha nacido")



# class Pajaro(Animal):
#     pass


# # Herencias de 'Pajaro'
# print(Pajaro.__bases__)
# # Subclases de 'Animal'
# print(Animal.__subclasses__())


# piolin = Pajaro(2, "Amarillo")
# print(piolin.color)



# # HERENCIA EXTENDIDA -----------

# class Animal:

#     def __init__(self, edad, color):
#         self.edad = edad
#         self.color = color


#     def nacer(self):
#         print("El animal ha nacido")
    

#     def hablar(self):
#         print("Este animal emite un sonido")


# class Pajaro(Animal):
#     def __init__(self, edad, color, altura_vuelo):
#         super().__init__(edad, color)
#         self.altura_vuelo = altura_vuelo

#     def hablar(self):
#         print("Pio")

    
#     def volar(self, metros):
#         print(f"El pajaro vuela a {metros} metros")


# piolin = Pajaro(2, "Amarillo", 234)

# piolin.hablar()


# ---------------------------------
# class Padre:
#     def hablar(self):
#         print("Hola")


# class Madre:
#     def reir(self):
#         print("jajajajaja")

#     def hablar(self):
#         print("Que tal")

# class Hijo(Padre, Madre):
#     pass


# class Nieto(Hijo):
#     pass


# nieto = Nieto()
# # Hereda los metodos que primero fueron pasados
# nieto.hablar()
# nieto.reir()

# # Method Order Resolution -> Orden Herencia Metodos
# Metodo orden busqueda metodos heredados
# print(Nieto.__mro__)


# # EJERCICIOS ---------------

# class Persona:
#     def __init__(self, nombre, edad):
#         self.nombre = nombre
#         self.edad = edad


# class Alumno(Persona):
#     pass

# class Vertebrado:
#     vertebrado = True

# class Ave(Vertebrado):
#     tiene_pico = True
#     def poner_huevos(self):
#         print("Poniendo huevos")

# class Reptil(Vertebrado):
#     venenoso = True

# class Pez(Vertebrado):
#     def nadar(self):
#         print("Nadando")
#     def poner_huevos(self):
#         print("Poniendo huevos")

# class Mamifero(Vertebrado):
#     def caminar(self):
#         print("Caminando")
#     def amamantar(self):
#         print("Amamantando crías")

# class Ornitorrinco(Ave, Pez, Reptil, Mamifero):
#     def __init__(self):
#         super().__init__()


# ornitorrinco = Ornitorrinco()
# ornitorrinco.poner_huevos()



# class Padre():
#     color_ojos = "marrón"
#     tipo_pelo = "rulos"
#     altura = "media"
#     voz = "grave"
#     deporte_preferido = "tenis"
#     def reir(self):
#         return "Jajaja"
#     def hobby(self):
#         return "Pinto madera en mi tiempo libre"
#     def caminar(self):
#         return "Caminando con pasos largos y rápidos"
        
# class Hijo(Padre):
#     def __init__(self):
#         super().__init__()

#     def hobby(self):
#         return "Juego videojuegos en mi tiempo libre"

# hijo = Hijo()

# print(hijo.reir())


# POLIMORFISMO ---------------------------------------
# POLI -> MUCH@S
# MORFISMO -> FORMAS 

# class Vaca:
#     def __init__(self, nombre):
#         self.nombre = nombre

#     def hablar(self):
#         return f"{self.nombre} dice muuuu"


# class Oveja:
#     def __init__(self, nombre):
#         self.nombre = nombre

#     def hablar(self):
#         return f"{self.nombre} dice beeee"


# vaca1 = Vaca("Aurora")
# oveja1 = Oveja("Nube")

# animales = [vaca1, oveja1]


# # Polimorfismo -------------------- 
# # EJEMPLO - (Ejecutar metodos con mismo nombre)
# # for animal in animales:
# #     print(animal.hablar())


# def animal_habla(animal):
#     return animal.hablar()


# print(animal_habla(vaca1))
# print(animal_habla(oveja1))


# METODOS ESPECIALES (MAGI METHODS) ----------------------------

class CD:
    
    def __init__(self, autor, titulo, canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones

    def __str__(self):
        return f"{self.autor} - {self.titulo} - {self.canciones}"

    def __len__(self):
        return self.canciones 

    def __del__(self):
        print(f"Se ha eliminado {self.titulo}.")


mi_cd = CD("Pink Floyd", "The Wall", 24)

print(str(mi_cd)) # o print(mi_cd)
print(len(mi_cd))

del mi_cd