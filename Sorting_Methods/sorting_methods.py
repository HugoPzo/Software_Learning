import os
import random
import time


def user_number():
    number = None
    while not number:
        try:
            number = int(input("Enter how much numbers will be order: "))
        except ValueError:
            os.system("cls")
            print("Enter numbeeeers!!!")
    return number


def random_list(user_number):
    num_list = list()
    while len(num_list) < user_number:
        num = random.randint(0, user_number)
        if num not in num_list:
            num_list.append(num)
    return num_list


def bubble_sort(number_list):

    print("--------------------Bubble Sort--------------------")
    print(number_list)
    list_len = len(number_list)

    t1 = time.time()

    for i in range(list_len):
        for j in range(list_len-i-1):
            if number_list[j] > number_list[j + 1]:
                number_list[j], number_list[j + 1] = number_list[j + 1], number_list[j]

    t2 = time.time()

    print(f"The ordering take {t2-t1} seconds.")

    return number_list


def insertion_sort(number_list):
    pass


def selection_sort(number_list):
    pass


def merge_sort(number_list):
    pass


def quick_sort(number_list):
    pass


def main():
    # User number
    user_num = user_number()

    # Lists
    bubble_sort_list = random_list(user_num)
    insertion_sort_list = random_list(user_num)
    selection_sort_list = random_list(user_num)
    merge_sort_list = random_list(user_num)
    quick_sort_list = random_list(user_num)


    # Methods

    # Bubble Sort
    print(bubble_sort(bubble_sort_list))
    print("\n")

    # Insertion Sort
    # Selection Sort
    # Merge Sort
    # Quick Sort



if __name__ == "__main__":
    main()

