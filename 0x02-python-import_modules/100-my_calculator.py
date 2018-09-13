#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    op = argv[2]
    num1 = int(argv[1])
    num2 = int(argv[3])

    if op is '+':
        print("{:d} + {:d} = {:d}".format(num1, num2, add(num1, num2)))
    elif op is '-':
        print("{:d} - {:d} = {:d}".format(num1, num2, sub(num1, num2)))
    elif op is '*':
        print("{:d} * {:d} = {:d}".format(num1, num2, mul(num1, num2)))
    elif op is '/':
        print("{:d} / {:d} = {:d}".format(num1, num2, div(num1, num2)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
