# +++++++++Logical Operators+++++++++
# 11

# (and, or, not) = used to check if two or more conditional statements

temp = int(input("What is the temperature outside?: "))

if temp >= 0 and temp <= 30:
    print("The temperature is good outside!"
          "\nGo outside")
elif temp < 0 or temp > 30:
    print("The temperature is bad outside!"
          "\nStay inside")



temp_2 = int(input("What is the temperature outside?: "))

# 'not' operator change the sense of the boolean operators
# If the conditon is 'True' the condition 'not' change it to 'False'

if not(temp_2 >= 0 and temp_2 <= 30):
    print("The temperature is good outside!"
          "\nGo outside")
elif not(temp_2 < 0 or temp_2 > 30):
    print("The temperature is bad outside!"
          "\nStay inside")
