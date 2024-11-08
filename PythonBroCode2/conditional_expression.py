# condition expression = A one line shortcut for the if-else statement
                        # (ternary operator)
                        # Print or assign one of two values based on a
                        # condition
                        # X if condition else Y


# 'X' if condition else 'Y'

num = 6


print("Positive" if num > 0 else "Negative")
result = "EVEN" if num % 2 == 0 else "ODD"
print(result)

a = 6
b = 32
max_num = a if a > b else b
min_num = a if a < b else b
print(max_num)
print(min_num)

age = 32
status = "Adult" if age >= 18 else "Child"
print(status)

temperature = 12
weather = "Hot" if temperature >= 30 else "Cold"
print(weather)

user_access = "user"
access = "Full Access" if user_access == "admin" else "Limited Access"
print(access)