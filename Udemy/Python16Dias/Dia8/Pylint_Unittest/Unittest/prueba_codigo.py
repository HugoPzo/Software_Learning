import unittest
import codigo # Importar Modulo a testear

# Creamos clase que haga las pruebas, heredamos clases de 'unittest' 
class Prueba(unittest.TestCase):
    # Funcion que se encargue de hacer la verificacion

    # TODAS LAS FUNCIONES DE TESTEO DEBEN EMPEZAR CON 'test' - E.G = test_nombre
    def test_mayusculas(self):
        # Testeo de codigo

        # Caso funcion de modulo seleccionado
        palabra = 'buen dia'
        resultado_codigo = codigo.todo_mayus(palabra)

        # Metodo que chequea dos argumentos, deben ser iguales con este metodo en especifico - Devuelve un error si no es correcto

        # RESULTADO DEL CODIGO  # COMO DEBE SER
        self.assertEqual(resultado_codigo, 'BUEN DIA')

        # Se puede agregar un tercer parametro 'mensaje' en este caso, nos devuelve un string con la informacion del error
        # self.assertEqual(resultado_codigo, 'BUEN DIA', mensaje)


"""Antes incluso de ejecutar el código, Python lee el archivo para definir algunas variables globales. Una de ellas es
__name__, que toma el nombre "__main__" en caso que Python esté corriendo en dicho módulo de manera
individual. Si por el contrario, el módulo fuera importado, la variable __name__ toma el nombre del módulo. Este bloque
de código evalúa que la prueba se esté ejecutando directamente"""

if __name__ == "__main__":
    # Ejecutamos este modulo como el principal
    unittest.main()    
