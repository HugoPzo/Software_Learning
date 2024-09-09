# map() = applies a function to each item in an iterable (list, tuple, etc.)
#
# map (function, iterable)

# Apply Something

store = [("shirt", 17),
         ("pants", 22),
         ("jacket", 45),
         ("hoodie", 32),
         ("socks", 5)]


dollar_to_euro = 0.82

# Value of items in euros

# Access to the tuple by a lambda expression
store_items_to_euros = lambda item:(item[0], item[1]*dollar_to_euro)
# Apply a function to each element of the tuple
# Also can be used with list or other iterable
list_of_item_in_euros = list(map(store_items_to_euros, store))
[print(i) for i in list_of_item_in_euros]
print("\n")


# Value of items in dollars
# round(number, digits)
store_items_to_dollars = lambda item:(item[0], round((item[1]/dollar_to_euro), 2))
list_of_item_in_dollars = list(map(store_items_to_dollars, store))
[print(i) for i in list_of_item_in_dollars]
