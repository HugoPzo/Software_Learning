# Both works the same

# Multihilos : Procesos I/O (Input / Output)
# Multiprocesamiento : Procesos de alta exigencia

# Each thread can carry out its own order of instructions

# thread = a flow of execution. Like a separate order of instructions
          # However each thread takes a turn running to achieve concurrancy
          # GIL = (Global interpreter lock),
          # allows only one thread to hold


# cpu bound = program/task spends most of it's time waiting for internal events
            # (CPU intensive)

# io bound = program/task spends most of it's time waiting for external events (user input, web scraping)
            # use multithreading

from multiprocessing import Process, cpu_count
import threading
import time


def counter(num):
    cnt = 0
    while cnt < num:
        cnt += 1

def main():


    # This process has a limit, cores of the cpu

    # Nucleos del procesador
    print(cpu_count())
    # Number of active threads
    print(threading.active_count())
    # In this case, return the 'Main Thread' that is running the main program
    print(threading.enumerate())

    # Starting counter of time
    start = time.perf_counter()

    # We open multiple cores to execute a process, this allow us
    #   executing faster a program.

    # Both ways to carry out multiprocessing
    thread1 = threading.Thread(target=counter, args=(500000000,))
    process1 = Process(target=counter, args=(500000000,))
    # Start the other cores
    thread1.start()
    process1.start()
    # The main process waits until the cores end the process
    thread1.join()
    process1.join()

    end = time.perf_counter()

    # Print the time that takes the process
    print(f"{end-start} seconds...")


if __name__ == "__main__":
    main()