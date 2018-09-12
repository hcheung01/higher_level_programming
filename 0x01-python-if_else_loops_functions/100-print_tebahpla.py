#!/usr/bin/python3
for i in range(122, 96, -1):
    if i % 2 is 0:
        num = i
    else:
        num = i - 32
    print("{:s}".format(chr(num)), end="")
