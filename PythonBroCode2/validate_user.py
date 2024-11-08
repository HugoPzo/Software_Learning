# Validate User Input Exercise


# 1. User is no more than 12 characters
# 2. Username must not contain spaces
# 3. Username must not contain digits

username = input("Enter a username: ")



if len(username) > 12:
    print("Username must contain less than 12 characters")
elif not username.find(" ") == -1:
    print("Username can't contain spaces")
elif not username.isalpha():
    print("Username can't contain digits")
else:
    print(f"Welcome {username}")
