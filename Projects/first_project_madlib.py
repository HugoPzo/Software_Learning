import Presentation as Pr

Pr.presentationBox("Mad Lib", "1")

name = input("Enter name: ")
age = int(input("Enter your age: "))
football_player = input("Enter your favorite FootBall player: ")
def madLib(name, age, football_player):

    text = ("\nHello, this is my story. My name is {:^5}\n"
            "I'm {:>4b} old. My favorite football player is {}".format(name[::-1], age,
                                                                       football_player.capitalize()))


    return print(text)


madLib(name, age, football_player)