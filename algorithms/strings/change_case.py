# Simple function that converts uppercase characters to lowercase and vice versa.
# Author: jotslo

def change_case(string):
    # Iterates through string, if character is lowercase, convert to upper else lower
    new_string = [char.upper() if char.islower() else char.lower() for char in string]

    # Joins list with an empty string to form the new string and return
    return "".join(new_string)

print(change_case("Hello, world!")) # hELLO, WORLD!
print(change_case("TEST")) # test
