# +++++++++Strip+++++++++

# strip() = delete all the white spaces


user_input = input("Enter a text with space: ")


# Delete all the white spaces from the input "left & right"
print(user_input.strip())
# Delete all the white spaces from the input "left"
print(user_input.lstrip())
# Delete all the white spaces from the input "right"
print(user_input.rstrip())
