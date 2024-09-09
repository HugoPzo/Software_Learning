import os
import random
import time
from concurrent.futures import ThreadPoolExecutor


def user_leng_list():
    user_input = None

    while not user_input:
        try:
            user_input = int(input("Enter the length of your list: "))
        except ValueError:
            os.system("cls")
            print("Enter a number...")
    return user_input


def create_random_list(leng_list):
    random_list = []
    while len(random_list) < leng_list:
        num = random.randint(1, leng_list)
        if num not in random_list:
            random_list.append(num)
    return random_list


def quick_sort(list_to_order):

    order_list = list_to_order.copy()

    lista_A, lista_B, lista_C = [], [], []

    for num in order_list:
        if num < (len(order_list)//2):
            lista_A.append(num)
        else:
            lista_B.append(num)

    def order_listA(lista_A):
        ord_ls = lista_A.copy()
        len_list = len(ord_ls)

        for i in range(len_list):
            for j in range(len_list-i-1):
                if ord_ls[j] > ord_ls[j+1]:
                    ord_ls[j], ord_ls[j+1] = ord_ls[j+1], ord_ls[j]
        return ord_ls



    def order_listB(lista_B):
        ord_ls = lista_B.copy()
        len_list = len(ord_ls)

        for i in range(len_list):
            for j in range(len_list - i - 1):
                if ord_ls[j] > ord_ls[j + 1]:
                    ord_ls[j], ord_ls[j + 1] = ord_ls[j + 1], ord_ls[j]
        return ord_ls



    with ThreadPoolExecutor() as executor:
        a = executor.submit(order_listA, lista_A)
        b = executor.submit(order_listB, lista_B)
        result_a = a.result()
        result_b = b.result()

    final_result = []
    final_result += result_a + result_b

    return final_result


def main():
    list_to_order = create_random_list(user_leng_list())
    t1 = time.time()
    order_list = quick_sort(list_to_order)
    t2 = time.time()

    print(list_to_order)
    print(order_list)
    print(f"Time to order: {t2-t1} seconds1")

if __name__ == "__main__":
    main()