from sys import platform
from os import system

# Check operating system to clean terminal
def check_system_clean():
    # Linux or OS
    if platform == "linux" or platform == "linux2" or platform == "darwin":
        return system("clear")
    # Windows
    elif platform == "win32":
        return system("cls")
