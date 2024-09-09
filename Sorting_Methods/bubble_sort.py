# -------Bubble Sort-------


import time
num_list = [5, 2, 8, 23, 7, 3, 9, 12, 1]

n = len(num_list)
print(f"{n}\n")

# Start time
t1 = time.time()

for i in range(n):
    for j in range(n-i-1):
        if num_list[j] > num_list[j+1]:
            num_list[j], num_list[j+1] = num_list[j+1], num_list[j]


# Finish time
t2 = time.time()
print(f"Took {t2-t1} seconds")

print(num_list)