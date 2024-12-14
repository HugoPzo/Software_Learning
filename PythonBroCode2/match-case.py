# Match-case statement (switch): An alternative to using
#            many  'elif' statements
#            Execute some code if a value matches a 'case'
#            Benefits: cleaner and syntax is more readable


# match variable:
#     case -:
#        code

def day_of_week(day):
    match day: # Match a variable
        case 1:
            return "It is Sunday"
        case 2:
            return "It is Monday"
        case 3:
            return "It is Tuesday"
        case 4:
            return "It is Wednesday"
        case 5:
            return "It is Thursday"
        case 6:
            return "It is Friday"
        case 7:
            return "It is Saturday"
        case _:      # ---> 'else' statement
            return "Not a valid day"


print(day_of_week(5))


def is_weekend(day):
    match day.capitalize(): # Match a variable
        case "Saturday" | "Sunday":
            return True
        case _:
            return False


print(is_weekend("monday"))