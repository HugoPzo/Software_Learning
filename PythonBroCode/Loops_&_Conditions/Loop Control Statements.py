# +++++++++Loop Control Statements+++++++++


# Change a loops execution from its normal sequence


#   break =   used to terminate the loop entirely
#   continue =  skips to the next iteration of the loop
#   pass =  does nothing, acts as a placeholder


# Break
while True:
    name = input("Enter your name: ")
    if name != "":
        break

print("\n")


# Continue

phone_number = "123-456-7890"

# If there is a '-' the loop just continue, so it errase the hyphen
for i in phone_number:
    if i == "-":
        continue
    print(i, end="")

print("\n")

# Pass

for i in range(1, 21):
    if i == 13:
        pass
    else:
        print(i, end=" ")