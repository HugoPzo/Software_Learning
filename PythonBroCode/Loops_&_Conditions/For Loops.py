# +++++++++For Loops+++++++++
# 10

# for loop =     a statement that will execute it's block of code
#                a limited amount of times

#               while loop = unlimited
#               for loop = limited


for i in range(10):
    print(i+1)

print("\n")

# Print from 50 to 100
for j in range(50, 100+1):
    print(j)

print("\n")

# Print from 50 to 100 with a step of 2
for k in range(50, 100+1,2):
    print(k)

print("\n")

for l in "Hugo Perez":
    print(l)

print("\n")

import time


# Prints from 10 to 1 in reverse order
for seconds in range(10, 0, -1):
    print(seconds, end=" ")
    time.sleep(1)

print("Happy New Year!!")