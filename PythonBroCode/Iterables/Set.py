# +++++++++Set+++++++++

# Set = collection which is unordered, unindexed. No duplicate values

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "cup", "plate", "knife"}

# If we print, the order won't be necessary the
# same as it was established

# Faster than a list and don't allow duplicate values
for x in utensils:
    print(x)

# Only will be printed one 'Knife'
utensils_2 = {"fork", "spoon", "knife", "knife", "knife"}

for x in utensils_2:
    print(x)


# Methods

utensils.add("napkin")
utensils.remove("fork")
utensils.clear()
utensils.update(dishes)

dinner_table = utensils.union(dishes)

# Compare similarities and differences
utensils.difference(dishes)
dishes.intersection(utensils)


for x in utensils:
    print(x)



