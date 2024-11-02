import random
from tkinter import *

def next_turn(row, column):

    global player

    if buttons[row][column]['text'] == "" and check_winner() is False:

        if player == players[0]:

            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[1]
                player_text.config(text=f"{player} turn")

            elif check_winner() is True:
                player_text.config(text=f"{player} wins!!")

            elif check_winner() == "Tie":
                player_text.config(text="Tie!!")

        else:

            buttons[row][column]["text"] = player

            if check_winner() is False:
                player = players[0]
                player_text.config(text=f"{player} turn")
            elif check_winner() is True:
                player_text.config(text=f"{player} wins!!")
            elif check_winner() == "Tie":
                player_text.config(text="Tie!!")


def check_winner():
    global player

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

    print(spaces)
    if spaces == 0:
        return False



def new_game():
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
player = random.choice(players)


player_text = Label(window, text=f"'{player}' Turn", font=("Constantia", 25), pady=10, padx=10, bg="#000", fg="#0F0")
player_text.pack(side=TOP)


reset_button = Button(window, text="RESET", font=("Constantia", 15), command=new_game, bg="#000", fg="#0F0")
reset_button.pack(side=BOTTOM)

buttons_frame = Frame(window)
buttons_frame.pack()

buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

for row in range(3):
    for column in range(3):
        # Each (x, y) has his button
        buttons[row][column] = Button(buttons_frame, font=("Constantia", 10),
                                      width=14, height=8, bg="#000", fg="#0F0",
                                      command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)

print(buttons)

window.mainloop()