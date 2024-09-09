# ***********************
# Python multiprocessing
# ***********************

# multiprocessing = running tasks in parallel on different cpu cores
#                   bypasses GIL used for threads

#   multiprocessing = better for cpu bound tasks (heavy cpu usages)
#   multithreading = better for io bound tasks (waiting around)

from multiprocessing import Process, cpu_count
import time

def counter(num):
    count = 0

    while count < num:
        count += 1


def main():

    # The amount of Process depends on the cores of the CPU
    print(cpu_count())

    t1 = time.time()
    a = Process(target=counter, args=(250000000,))
    b = Process(target=counter, args=(250000000,))
    c = Process(target=counter, args=(250000000,))
    d = Process(target=counter, args=(250000000,))
    a.start()
    b.start()
    c.start()
    d.start()
    a.join()
    b.join()
    c.join()
    d.join()

    print(a)

    t2 = time.time()

    print(f"{t2-t1} seconds...")




# Must to add
if __name__ == '__main__':
    main()