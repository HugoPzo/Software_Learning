import time 
import timeit # Evalua tiempo de ejecucion del codigo

def prueba_for(numero):
    lista = []
    for num in range(1, numero + 1):
        lista.append(num)
    return lista


def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista


def main():
    # # TIME
    # ## MEDIR TIEMPO CON MODULO 'time' 

    # FOR
    # inicio = time.time()
    # prueba_for(100000)
    # final = time.time()

    # print(f"For Loop {final - inicio}")
    
    # print("\n")
    
    # WHILE
    # inicio = time.time()
    # prueba_while(100000)
    # final = time.time()
    # print(f"While Loop {final - inicio}")


    # TIMEIT - IDENTIFICAR TIEMPO DE EJECUCION CON UN CODIGO ESPECIFICO
    ## MEDIR TIEMPO CON MODULO 'timeit'       
    
    # timeit.timeit(stmt, setup, timer, number)
    # stmt = statement (declaracion)
    # setup =
    # number = Cuantas veces deseamos que se ejecute el codigo

    number = 10000000 # Numero de veces que deseamos que se repita el codigo

    ### FOR -------------------------------------------------

    for_stmt = """prueba_for(100)""" # Statement - Llamada a Funcion 

    # CAREFUL WITH INDENTATION
    for_setup = """
def prueba_for(numero):
    lista = []
    for num in range(1, numero + 1):
        lista.append(num)
    return lista""" # Setup - Funcion

    
    duracion_for = timeit.timeit(for_stmt, for_setup, number=number)
    print(duracion_for) # 0.20389199999772245

    ### WHILE -------------------------------------------------

    while_stmt = """prueba_while(100)""" # Statement - Llamada a Funcion 

    # CAREFUL WITH INDENTATION
    while_setup = """
def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista""" # Setup - Funcion

    
    duracion_while = timeit.timeit(while_stmt, while_setup, number=number)
    print(duracion_while) # 0.2799933999995119



if __name__ == "__main__":
    main()