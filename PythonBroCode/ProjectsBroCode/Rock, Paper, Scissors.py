import random

def play_again():
    choices = ["Y", "N"]
    player_choice = None
    result = True

    while player_choice not in choices:
        try:
            player_choice = input("Want to play again? [Y/N]:").upper()

            if player_choice == "N":
                result = False

        except ValueError:
            print("Choose Y or N")

    return result


choices = {0: "Rock",
           1: "Scissors",
           2: "Paper"}


play = None

while play != False:

    user_choice = None
    computer_choice = random.randint(0, 2)

    options = [0, 1, 2]

    while user_choice not in options:
        try:
            user_choice = int(input("Choose one option:\n"
                                    "[0] Rock\n"
                                    "[1] Scissors\n"
                                    "[2] Paper\n"
                                    ":"))
            result = (user_choice-computer_choice)%3
            if user_choice in options:
                print(f"You choose {choices.get(user_choice)}")
                print(f"Your opponent choose {choices.get(computer_choice)}")
                if result == 0:
                    print("Empate")
                    play = play_again()
                else:
                    if result == 1:
                        print("Computer Wins!")
                        play = play_again()
                    else:
                        print("You Win!")
                        play = play_again()
        except ValueError:
            print("Choose one number!!!\n")