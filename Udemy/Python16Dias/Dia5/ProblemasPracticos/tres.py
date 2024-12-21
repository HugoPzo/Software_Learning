def two_zeros(*args):
    lista_numeros = list(args)
    for i in lista_numeros:
        pointer = lista_numeros.index(i)
        if i == 0 and lista_numeros[pointer+1] == 0:
            return True
    return False
        


def main():
    print(two_zeros(4, 6, 0, 0, 9, 3, 0, 1, 3, 5))
    print(two_zeros(4, 6, 7, 8, 9, 3, 0, 1, 3, 5))
    print(two_zeros(4, 6, 7, 8, 9, 3, 0, 1, 3, 5))
    print(two_zeros(4, 6, 7, 8, 9, 3, 0, 0, 3, 5))


if __name__ == "__main__":
    main()