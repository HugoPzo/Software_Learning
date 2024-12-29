# # I / O -> Input / Output
#

#
# # Only Read the file
# my_file_read = open("prueba.txt", 'r')
# # Delete and Write
# my_file_write = open("prueba.txt", 'w')
# # Add write on the end of the text
# my_file_add = open("prueba.txt", 'a')

#
# # READ **********************************************************
#
#
# my_file = open('prueba.txt', 'r')
#
#
# # All lines
# print(my_file.read())
# # Read one line
# print(my_file.readline())
#
# # Lines in a list
# print(my_file.readlines())
#
# # Boolean, if it's possible to read
# print(my_file.readable())
#
#
# my_file.close()

# ## Read a specific line
# # importing required package
# import linecache
#
# # extracting the 5th line
# particular_line = linecache.getline('prueba.txt', 2)
#
# # print the particular line
# print(particular_line)

#
# # **********************************************************

# # # CREAR Y ESCRIBIR ARCHIVOS
#
#
# my_file = open('prueba.txt', 'w')
# my_file.write("Im the new text")
# my_file.close()
#
# lista = ["1", "2", "3", "4", "5", "6", "7", "8"]
#
# my_file = open('prueba.txt', 'w')
# for i in lista:
#     my_file.write(i + "\n")
# my_file.close()
#
#
#
# my_file = open('prueba.txt', 'a')
# my_file.write("Im the new text 2 ")
# my_file.close()



