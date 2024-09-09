# +++++++++Dictionaries+++++++++

# A changable, unordered collection of unique
# (key:value) pairs
# Fast because they use hashing, allow us to
# access a value quickly


capitals = {'USA': 'Washington DC',
            'India': 'New Dehli',
            'China': 'Beijing',
            'Russia': 'Moscow'}

# Size of object in memory, in bytes.
print(capitals.__sizeof__())

# Update the dictionary with a new key:value
capitals.update({'Germany':'Berlin'})
# Also update existing keys
capitals.update({'USA':'Las Vegas'})
# Remove a key and value
capitals.pop('China')

# Clear the dictionary
#capitals.clear()


"""To get the value of one key, we can use "[]"
but it's not the recommended way because if the
value doesn't exist it will return a Error"""
#print(capitals['Germany'])

# The recommended way is to use .get(), if the key
# doesn't exist, will return 'None'
print(capitals.get('Germany'))

# Keys from the dictionary
print(capitals.keys())
# Values from the keys
print(capitals.values())
# Keys and Values
print(capitals.items())

# Loop to print dictionary
for key, value in capitals.items():
    print(f"{key}:{value}")