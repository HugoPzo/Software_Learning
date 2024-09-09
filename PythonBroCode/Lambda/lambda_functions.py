import functools
import random

friends = [("Rachel", 21, 54),
            ("Lebron", 15, 23),
            ("Kobe", 17, 36),
            ("Walgreens", 18, 51),
            ("Russ", 24, 19)]



# Order by Columns

order_friends = sorted(friends)

order_friends.sort()
[print(i) for i in order_friends]
print("\n")

ages = lambda age:age[1]
order_friends.sort(key=ages)
[print(i) for i in order_friends]
print("\n")

salaries = lambda salary:salary[2]
order_friends.sort(key=salaries)
[print(i) for i in order_friends]
print("\n")

# Order by filter()
order_by_18 = lambda x:x[1]>=18
list_18 = list(filter(order_by_18, friends))
[print(i) for i in list_18]
print("\n")

# Multiply map()
multi_ages = lambda x:(x[0], x[1]*2, x[2])
list_age_times_2 = list(map(multi_ages, friends))
[print(i) for i in list_age_times_2]
print("\n")

# reduce()
number_list = []
list_leng = 5
for i in range(list_leng):
    number_list.append(random.randint(1, list_leng))
print(number_list)

num = lambda x, y: x*y
result = functools.reduce(num, number_list)
print(result)