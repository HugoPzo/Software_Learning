# daemon thread = a thread that runs in the background, not important
#                  for program to run your program will not wait for daemon
#                  threads to complete before exiting.

#                  non-daemon threads cannot normally be killed,
#                  stay alive until task is complete.

#                  ex. background tasks: garbage collection, waiting for input
                    #  long running process


import threading
import time


def timer_non_daemon():
    counter = 0
    while True:
        time.sleep(1)
        counter += 1
        print(f"Im a non-daemon thread: {counter}")


def timer_daemon():
    counter = 0
    while True:
        time.sleep(1)
        counter += 1
        print(f"Im a daemon thread: {counter}")



# This process still be running after the input
x = threading.Thread(target=timer_non_daemon)
x.start()

# This process will be killed after the input
y = threading.Thread(target=timer_daemon, daemon=True)
y.start()

# Change non-daemon to daemon
x.setDaemon(True)
# Know if it is daemon or non-daemon
print(y.isDaemon())

user = input("Want to exit?")


