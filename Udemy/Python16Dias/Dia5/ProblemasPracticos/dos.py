
def letras_unicas(palabra):
    lista_letras = set()
    palabra = palabra.lower()
    for letra in palabra:
        lista_letras.add(letra)

    lista_letras = list(lista_letras)
    lista_letras.sort() 
    
    return lista_letras


def main():
    palabra = letras_unicas("entretenido")
    print(palabra)



if __name__ == "__main__":
    main()