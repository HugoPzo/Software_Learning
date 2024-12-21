import random

CHANCES = 8
user_answers = []
computer_number = random.randint(1, 100)
# print(computer_number)
print(f"YOU HAVE {CHANCES} CHANCES")


while len(user_answers) < CHANCES:
    try:
        user_answer = int(input("Enter a number between 1 and 100: "))
        user_answers.append(user_answer)
        
        if user_answer == computer_number:
            print("You won!!")
            break
        elif user_answer not in range(1, 101):
            print("ENTER A NUMBER BETWEEN 1 AND 100")
            user_answers.pop()
        elif user_answer > computer_number:
            print("Number is lower!")
        elif user_answer < computer_number:
            print("Number is higher!")
    except ValueError:
        print("Enter a valid number.")

if len(user_answers) == 8:
    print("You lose!!!")