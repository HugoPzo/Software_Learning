import random
from tkinter import *



# Canvas size - Game Size
GAME_WIDTH = 700
GAME_HEIGHT = 700

# Speed of the snake (How often canvas will update)
# Lower the number -> Faster the game
SPEED = 80
# Space of each item
# How large are the items in the game (Food, Body Parts of snake)
SPACE_SIZE = 50 # Like a chess board

# GAME Configuration
# How many body parts does the snake will havve starting the game
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
GAME_BACKGROUND = "#000000"


class Snake:

    def __init__(self):
        self.body = BODY_PARTS
        self.coordinates = []
        self.squares = []

        # List of coordinates
        # Each Body Part have his own coordinates
        for i in range(0, BODY_PARTS):
            # Starting point -> Top Left
            self.coordinates.append([0,0])


        # coordinates[0] -> Head of the snake

                            # Coordinates
        # Coordinates x, y in [[x,y],[x,y],[x,y]]:
        for x, y in self.coordinates:
            # Create a square for each coordinate
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y+SPACE_SIZE, fill=SNAKE_COLOR,
                                             tags="snake")
            self.squares.append(square)


class Food:
    # Constructor
    def __init__(self):
    #   Game sizes are like rectangles in chessboard, so:
    #           GAME_WIDTH = 700 / 50 SPACE_SIZE -> Spots
                                # Choose random place * Pixels
        x = random.randint(0, (GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE

        # Coordinates is just a point in the canvas
        # Set food coordinates
        self.coordinates = [x, y]

        # Create a circle
        # tags = Identified the element
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tags="food")

# End Reset Game
def reset_game():

    # Set score to 0
    global score
    # Set score to down
    global direction

    score = 0
    label.config(text=f"Score: {score}")

    # Delete all in canvas
    canvas.delete(ALL)

    # Reset the direction
    direction = "down"


# Moving direction in every turn ---
def next_turn(snake, food):

    # Head of the snake
    x, y = snake.coordinates[0]

    # Head Moving Direction
    if direction == "up" or direction == "w":
        y -= SPACE_SIZE
        # Calculate collision borders to appear at the other side
        y %= GAME_HEIGHT
    elif direction == "down" or direction == "s":
        y += SPACE_SIZE
        y %= GAME_HEIGHT
    elif direction == "left" or direction == "a":
        x -= SPACE_SIZE
        x %= GAME_WIDTH
    elif direction == "right" or direction == "d":
        x += SPACE_SIZE
        x %= GAME_WIDTH


    # Update snake head coordinates
    # snake.coordinate[0] = Head Position
                       # Updated x, y
    snake.coordinates.insert(0, (x, y))
    # Append New Square on updated position
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
    # Insert in position (0(Square Head Snake), new square)
    snake.squares.insert(0, square)


    # If head coordinates == food coordinates
    if x == food.coordinates[0] and y == food.coordinates[1]:

        global score
        score += 1
        label.config(text=f"Score: {score}")

        # Delete food object with 'tag'
        canvas.delete("food")

        food = Food()

    # Will only delete the last body part(tail) of the snake if we do not eat food
    else:

        # Delete tail of the snake
        # Coordinates & Square
        del snake.coordinates[-1]
        # Delete from canvas tail square
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

        # Call again the function after SPEED Time
        #      after(time, call_function, args*)
                        # Just call the function game

    if check_collisions(snake):
        game_over()
    else:
        window.after(SPEED, next_turn, snake, food)


def change_direction(new_direction):
    # Old direction
    global direction

    # Left
    if new_direction == "left" or new_direction == "a":
        # If old direction != right
        # Not allowing to go backwards, not to make a 180° degree turn !!!!
        if direction != "right" and direction != "d":
            direction = new_direction
    # Right
    elif new_direction == "right" or new_direction == "d":
        if direction != "left" and direction != "a":
            direction = new_direction
    # Up
    elif new_direction == "up" or new_direction == "w":
        if direction != "down" and direction != "s":
            direction = new_direction
    # Down
    elif new_direction == "down" or new_direction == "s":
        if direction != "up" and direction != "w":
            direction = new_direction


def check_collisions(snake):
    x, y = snake.coordinates[0]

    # For each coordinate in snake coordinates
    #                               Start after the head
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False


def game_over():
    # Delete all from canvas
    canvas.delete(ALL)
    # Center text in canvas
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                       font=("Bell MT", 70), text="GAME OVER", fill="red", tags="gameover")


window = Tk()

window.title("Snake Game")
# No resize the window
window.resizable(False, False)


# Score Label
score = 0
# Initial Direction
direction = "down"

label = Label(window, text=f"Score: {score}", font=("Bell MT", 40))
label.pack(side=TOP)

# Pack Correctly reset button ----
# RESET BUTTON
"""button = Button(window, background=GAME_BACKGROUND, width=GAME_WIDTH, text="RESET",
                fg="#0F0", font=(40), activeforeground="#F00", activebackground="#100",
                command=reset_game)
button.pack()"""

# CANVAS
# Set canvas Width & Height
canvas = Canvas(window, background=GAME_BACKGROUND, width=GAME_WIDTH, height=GAME_HEIGHT)
canvas.pack()

# Update Window so that it renders
window.update()


# Center the window
x = int((window.winfo_screenwidth()/2) - (GAME_WIDTH/2))
y = int((window.winfo_screenheight()/2) - (GAME_HEIGHT/2))
window.geometry(f"{GAME_WIDTH}x{GAME_HEIGHT}+{x}+{y}")

# Call to function at the time
# First one with argument 'event'
# Sercond one with argument requires
# window.bind("<Key>", lambda argument: function_called(argument)
# Left
window.bind("<Left>", lambda event: change_direction("left"))
window.bind("<a>", lambda event: change_direction("a"))
# Right
window.bind("<Right>", lambda event: change_direction("right"))
window.bind("<d>", lambda event: change_direction("d"))
# Up
window.bind("<Up>", lambda event: change_direction("up"))
window.bind("<w>", lambda event: change_direction("w"))
# Down
window.bind("<Down>", lambda event: change_direction("down"))
window.bind("<s>", lambda event: change_direction("s"))


snake = Snake()
food = Food()
# Call Function to update
next_turn(snake, food)

window.mainloop()