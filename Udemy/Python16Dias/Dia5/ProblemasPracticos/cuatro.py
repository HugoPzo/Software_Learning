def contar_primos(numero):
    lista_primos = [2]
    iteracion = 3


    if numero < 2:
        lista_primos = []
        return len(lista_primos)
    
    while iteracion <= numero:
        
        for n in range(3, iteracion, 2):

            if (iteracion % n) == 0:
                iteracion += 2
                break

        else:
            lista_primos.append(iteracion)
            iteracion += 2
    
            
    print(lista_primos)
    return len(lista_primos)
        
            

def main():
    print(contar_primos(50))
    print(contar_primos(3))
    print(contar_primos(13))
    print(contar_primos(2))


if __name__ == "__main__":
    main()