# +++++++++Random+++++++++

import random
# Pseudo-random numbers


# random.randint() solo genera números enteros, mientras que
# random.uniform(a, b) devuelve un número aleatorio
# de coma flotante en el rango especificado


x = random.randint(1, 9) # Random number from 1 to 9
print(x)
y = random.random() # Random number between 0 to 1
print(y)

u = random.uniform(2, 9) # Random floating number
print(u)

myList = ["rock", "paper", "scissors"]
z = random.choice(myList)
print(z)

# randrange(start, stop, [step])
t = random.randrange(0, 10, 2)
print(t)

# Schuffle the cards
# Barajar las cartas
cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]

random.shuffle(cards)

print(cards)