import random
import time
from tkinter import *


def next_turn(row, column):

    global player

    if buttons[row][column]['text'] == "" and check_winner() is False:

        if player == user:

            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = computer
                buttons_used.append(buttons[row][column])
                print(buttons_used)
                player_text.config(text="Computer turn")
                computer_play()

            elif check_winner() is True:
                player_text.config(text="You win!!")

            elif check_winner() == "Tie":
                player_text.config(text="Tie!!")




def computer_play():

    global player

    button_chosen = False
    while button_chosen == False:

        random_row = random.randint(0, 2)
        random_column = random.randint(0, 2)
        computer_button = buttons[random_row][random_column]


        if computer_button not in buttons_used:

            computer_button['text'] = player

            if check_winner() is False:
                player = user
                buttons_used.append(computer_button)
                print(buttons_used)
                player_text.config(text="User turn")


            elif check_winner() is True:
                player_text.config(text="Computer wins!!")

            elif check_winner() == "Tie":
                player_text.config(text="Tie!!")

            button_chosen = True


def check_winner():

    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="#0F0")
            buttons[row][1].config(bg="#0F0")
            buttons[row][2].config(bg="#0F0")
            return True

    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="#0F0")
            buttons[1][column].config(bg="#0F0")
            buttons[2][column].config(bg="#0F0")
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="#0F0")
        buttons[1][1].config(bg="#0F0")
        buttons[2][2].config(bg="#0F0")
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="#0F0")
        buttons[1][1].config(bg="#0F0")
        buttons[2][0].config(bg="#0F0")
        return True

    elif empty_spaces() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="#A21")
        return "Tie"

    else:
        return False


def empty_spaces():

    spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1


    if spaces == 0:
        return False


def new_game():
    global buttons_used
    buttons_used = []
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#000")



window = Tk()

window.title("TIC-TAC-TOE")
window.config(bg="#000")

# Center the window without 'WIDTH & HEIGHT"
WINDOW_WIDTH = window.winfo_reqwidth()
WINDOW_HEIGHT = window.winfo_reqheight()
x = int((window.winfo_screenwidth() / 2) - (WINDOW_WIDTH / 2))
y = int((window.winfo_screenheight() / 2) - (WINDOW_HEIGHT / 2))

window.geometry(f"+{x}+{y}")

players = ["X", "O"]
user = players[0]
player = user
computer = players[1]


player_text = Label(window, text=f"'{player}' Turn", font=("Constantia", 25), pady=10, padx=10, bg="#000", fg="#0F0")
player_text.pack(side=TOP)


reset_button = Button(window, text="RESET", font=("Constantia", 15), command=new_game, bg="#000", fg="#0F0")
reset_button.pack(side=BOTTOM)

buttons_frame = Frame(window)
buttons_frame.pack()

buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]
buttons_used = []

for row in range(3):
    for column in range(3):
        # Each (x, y) has his button
        buttons[row][column] = Button(buttons_frame, font=("Constantia", 10),
                                      width=14, height=8, bg="#000", fg="#0F0",
                                      command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)



window.mainloop()