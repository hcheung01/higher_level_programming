#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number % 10
greater = "and is greater than 5"
lesser = "and is less than 6 and not 0"
equal = "and is 0"
if last > 5:
    final = greater
elif last < 6 and not 0:
    final = lesser
elif last == 0:
    final = equal
print("Last digit of", number, "is", last, final)
