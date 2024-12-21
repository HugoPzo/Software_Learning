def devolver_distintos(num1, num2, num3):

    lista_numeros = [num1, num2, num3]
    used_numbers = []

    max_number = max(lista_numeros)
    min_number = min(lista_numeros)
    mid_number = 0

    used_numbers.append(max_number)    
    used_numbers.append(min_number)

    for i in lista_numeros:
        if i not in used_numbers:
            mid_number = i
    
    suma = sum(lista_numeros)

    if suma > 15:
        return max_number
    elif suma < 10:
        return min_number
    elif suma >= 10 and suma <= 15:
        return mid_number


print(devolver_distintos(1, 9, 3))
