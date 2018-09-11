#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 5 is 0 and i % 3 is 0:
            word = "FizzBuzz"
        elif i % 5 is 0:
            word = "Buzz"
        elif i % 3 is 0:
            word = "Fizz"
        else:
            word = str(i)
        print("{:s}".format(word), end=" ")
