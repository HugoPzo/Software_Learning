# Bubble Sort

# Quick Sort

import time
import random


def user_input():
    user_number = None
    while not user_number:
        try:
            user_number = int(input("Enter the length of your list: "))
        except ValueError:
            print("Enter a numbeeer!")
    return user_number


def random_list(list_length):
    random_list = []
    while len(random_list) < list_length:
        new_number = random.randint(0, list_length)
        if new_number not in random_list:
            random_list.append(new_number)

    return random_list


def divide_list(num_list):
    list_A = []
    list_B = []

    final_list = []

    own_lista = num_list.copy()
    n = len(own_lista)

    for i in own_lista:
        if i < (n // 2):
            list_A.append(i)
        else:
            list_B.append(i)

    # ------- Ordenar Lista A -------
    len_lista_a = len(list_A)
    for i in range(len_lista_a):
        for j in range(len_lista_a - i - 1):
            if list_A[j] > list_A[j + 1]:
                list_A[j], list_A[j + 1] = list_A[j + 1], list_A[j]

    # ------- Ordenar Lista B -------
    len_lista_b = len(list_B)
    for i in range(len_lista_b):
        for j in range(len_lista_b - i - 1):
            if list_B[j] > list_B[j + 1]:
                list_B[j], list_B[j + 1] = list_B[j + 1], list_B[j]

    final_list += list_A + list_B

    return final_list


def main():
    num_list = random_list(user_input())
    t1 = time.time()
    sorted_list = divide_list(num_list)
    t2 = time.time()

    print(sorted_list)
    print(f"It takes {t2 - t1} seconds...")


if __name__ == "__main__":
    main()