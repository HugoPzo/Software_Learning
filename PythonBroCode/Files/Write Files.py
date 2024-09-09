# +++++++++Write Files+++++++++

# path = "C:\\Users\\hugop\\OneDrive\\Escritorio\\test.txt"
text = "Yooooo, you'll be the greatest guy in the world"
more_text = "\nYour grandma will be fine, he will get better"

# Write a file, must to add the name of the file to the path
with open("test.txt", "w") as file: # 'w' is the mode that we must add to write a file
    file.write(text)
# Also this lines will rewrite the file

with open("test.txt", "a") as file:  # 'a' is the mode that we use if we want to append more text
    file.write(more_text)


with open("test.txt", "r") as file:  # 'r' is the mode that is predetermined, is not necessary to write it
    file.read()



