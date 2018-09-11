#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        final = ((number * -1) % 10)
    elif number > 0:
        final = number % 10
    else:
        final = number
    print("{:d}".format(final), end="")
    return final
