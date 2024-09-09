# +++++++++Slicing Strings+++++++++
# Cortar Strings
# 6

# Creating a substring by extracting elements from another string
#                indexing[] or slice()
#                [start:stop:stop]

name = "Hugo Perez Ortiz"


#indexing[]
first_name = name[0:3]
print(first_name)

# It can also work without the starting '0'
# Python assume that it start with '0'
first_name_2 = name[:4]
print(first_name_2)


last_name = name[5:16]
print(last_name)


# As first_name, it work in the same way without ending the index
# Python assume the end of the length
last_name_2 = name[5:]
print(last_name_2)


# 'Step' print every char steping the character you chose
# Print every two Characters
funky_name = name[0:16:2]
print(funky_name)
funky_name_2 = name[0:16:3]
print(funky_name_2)
# Python Assume we are going from 0 to the last character
funky_name_3 = name[::2]
print(funky_name_3)

# Reverse name
reversed_name = name[::-1]
print(reversed_name)


# ----slice()----
# We can reuse slice()

website_1 = "http://www.google.com"
website_2 = "https://es.wikipedia.org"

# 'slice()' works the same as index[], but we use ',' instead of ':'

slice_website = slice(11, -4)

# We reuse the slice function

print(website_1[slice_website])

print(website_2[slice_website])

