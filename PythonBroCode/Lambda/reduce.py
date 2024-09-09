# reduce() = apply a function to an iterable and reduce it to a single
            # cumulative value.

            # Performs function on first two elements and repeats process until
            # 1 value remain

# reduce(function, iterable)

import functools


# CONCATENATE A WORD

say_hi = ["H", "E", "L", "L", "O"]

# Process:
# ["H", "E", "L", "L", "O"]
# ["HE", "L", "L", "O"]
# ["HEL", "L", "O"]
# ["HELL", "O"]
# ["HELLO"]


word = functools.reduce(lambda x, y: x+y, say_hi)
print(word)


# FACTORIAL

factorial = [5, 4, 3, 2, 1]

# Process
# [5, 4, 3, 2, 1]
# [20, 3, 2, 1]
# [60, 2, 1]
# [120, 1]
# [120]

result = functools.reduce(lambda x, y: x*y, factorial)
print(result)