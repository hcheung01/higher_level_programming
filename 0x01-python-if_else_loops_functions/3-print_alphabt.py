#!/usr/bin/python3
for i in range(97, 123):
    if chr(i) is 'e' or chr(i) is 'q':
        continue
    else:
        print("{:s}".format(chr(i)), end="")
