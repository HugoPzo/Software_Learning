from colored import Style, Fore, Back

color = f'{Style.BOLD}{Fore.RED}{Back.WHITE}'

print(f'{color}Hello World{Style.reset}')