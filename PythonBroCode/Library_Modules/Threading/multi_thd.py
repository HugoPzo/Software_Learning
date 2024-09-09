
import threading
import time


# Multithreading runs concurrently, but not in parallel
# Multiprocessing do it in parallel

def eat_breakfast():
    time.sleep(3)
    print("You finish eating breakfast.")
def drink_coffee():
    time.sleep(4)
    print("You finish drinking coffee.")


def study():
    time.sleep(5)
    print("You finish sleeping.")


# In the case we use only the main thread, the above functions, take 12 seconds
"""eat_breakfast()
drink_coffee()
study()
"""

t1 = time.time()

# Open different threads to target functions and do the process outside the
#   main Thread
x = threading.Thread(target=eat_breakfast)
x.start()
y = threading.Thread(target=drink_coffee)
y.start()
z = threading.Thread(target=study)
z.start()

x.join()
y.join()
z.join()


print(threading.active_count())
print(threading.enumerate())

t2 = time.time()
# Time it take to complete task
print(f"{t2-t1}")

