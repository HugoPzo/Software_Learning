# zip(*iterables) = aggregate elements from two or more iterables (list, tuples, sets, etc)
                    # creates a zip object with paired elements stores in tuples
                    # for each element

# Works with unlimited *iterables

# If list are odd, also works, but the odd item, doesn't pair with anything
user_names = ["Hugo", "RodriPez", "Tomas"]
passwords = ("paquito200", "feiwn!ds", "tudasle$")

user = zip(user_names, passwords)
user_list = list(zip(user_names, passwords))
user_dict = dict(zip(user_names, passwords))


[print(i) for i in user]
print("\n")
[print(i) for i in user_list]
print("\n")
[print(f"{key} : {value}") for (key, value) in user_dict.items()]