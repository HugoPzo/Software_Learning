# filter() = creates a collection of elements from an iterable for which a
#            function returns

# filter(function, iterable)

# Search Results

friends = [("Rachel", 21),
            ("Lebron", 15),
            ("Kobe", 17),
            ("Walgreens", 18),
            ("Russ", 24)]

# Filter who can enter to a social club (>=18)

drink_age = lambda age:age[1] >= 18

older_friends = sorted(list(filter(drink_age, friends)))
[print(friend) for friend in older_friends]

print("\n")
older_friends_age = older_friends
older_friends_age.sort(key= lambda byAge:byAge[1])
[print(i) for i in older_friends_age]
